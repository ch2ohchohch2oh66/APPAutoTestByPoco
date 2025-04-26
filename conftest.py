#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/26
# Description: Keep Hungry Keep Foolish

import threading
import time
import logging
import pytest

from moduls.android.common.poco_common import poco
from configs.android.ui_elements import PopupElements
from configs.other_configs import WaitTime

logger = logging.getLogger(__name__)

# 弹窗处理线程函数
def handle_popup(exit_event):
    """处理弹窗的线程函数"""
    while not exit_event.is_set():
        start_time = time.time()  # 记录开始时间
        while (time.time() - start_time) < WaitTime.MEDIUM and not exit_event.is_set():
            if poco(**PopupElements.ALLOW_ONCE).exists():
                try:
                    logger.info('检测到权限请求弹窗，点击"允许本次使用"')
                    poco(**PopupElements.ALLOW_ONCE).click()
                    time.sleep(WaitTime.ULTRA_SHORT)  
                except Exception as e:
                    logger.error(f"处理权限请求弹窗失败: {e}")
                break  # 处理完弹窗后退出当前循环
            if poco(**PopupElements.POOR_NETWORK).exists():
                try:
                    logger.info('检测到网络状况不佳弹窗，点击"关闭视频"')
                    poco(**PopupElements.CLOSE_VIDEO).click()
                    time.sleep(WaitTime.ULTRA_SHORT)  
                except Exception as e:
                    logger.error(f"处理网络状况不佳弹窗失败: {e}")
                break
            if poco(**PopupElements.NOTIFICATION).exists():
                try:
                    logger.info('检测到消息通知弹窗，点击"再想想"')
                    poco(**PopupElements.THINK_AGAIN).click()
                    time.sleep(WaitTime.ULTRA_SHORT)  
                except Exception as e:
                    logger.error(f"处理消息通知弹窗失败: {e}")
                break
            if poco(**PopupElements.NEXT_INSTALL).exists():
                try:
                    logger.info('检测到安装提示弹窗，点击"下次安装"')
                    poco(**PopupElements.NEXT_INSTALL).click()
                    time.sleep(WaitTime.ULTRA_SHORT)  
                except Exception as e:
                    logger.error(f"处理安装提示弹窗失败: {e}")
                break
            if poco(**PopupElements.UPDATE_NOW).exists():
                try:
                    logger.info('检测到更新提示弹窗，点击关闭按钮')
                    poco(**PopupElements.CLOSE_UPDATE).click()
                    time.sleep(WaitTime.ULTRA_SHORT)  
                except Exception as e:
                    logger.error(f"处理更新提示弹窗失败: {e}")
                break
            time.sleep(WaitTime.ULTRA_SHORT)  # 减少轮询频率

# 会话级别的fixture，用于处理弹窗
@pytest.fixture(scope="session", autouse=True)
def handle_popup_fixture():
    """自动启动和停止弹窗处理的会话级别fixture"""
    # 创建退出事件和线程
    exit_event = threading.Event()
    thread_handle_popup = threading.Thread(target=handle_popup, args=(exit_event,))
    thread_handle_popup.daemon = True
    
    # 启动线程
    logger.info("启动弹窗处理守护线程")
    thread_handle_popup.start()
    
    # 等待测试执行
    yield
    
    # 停止线程
    logger.info("停止弹窗处理守护线程")
    exit_event.set()
    thread_handle_popup.join(timeout=WaitTime.MEDIUM)