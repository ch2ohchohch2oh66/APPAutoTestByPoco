#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 弹窗处理模块

import logging
import threading
from time import sleep

from moduls.android.common.poco_common import *
from configs.android.ui_elements import PopupElements
from configs.android.other_configs import WaitTime

logger = logging.getLogger(__name__)

# 全局变量，用于控制弹窗处理线程
popup_handler_running = False
popup_handler_thread = None

def handle_popups():
    """处理各种弹窗的主函数"""
    global popup_handler_running
    
    while popup_handler_running:
        try:
            # 一次性权限弹窗处理（同时有"允许"和"禁止"按钮时，优先点击"允许"）
            if poco(**PopupElements.ALLOW).exists() and poco(**PopupElements.DENY).exists():
                poco(**PopupElements.ALLOW).click()
                logger.info('检测到一次性权限弹窗，已点击"允许"')
                sleep(WaitTime.SHORT)
                continue

            # 处理权限弹窗
            if poco(**PopupElements.ALLOW_ONCE).exists():
                poco(**PopupElements.ALLOW_ONCE).click()
                logger.info("处理权限弹窗：点击允许本次使用")
                continue
                
            # 处理网络状况提示
            if poco(**PopupElements.POOR_NETWORK).exists():
                poco(**PopupElements.CLOSE_VIDEO).click()
                logger.info("处理网络状况提示：关闭视频")
                continue
                
            # 处理消息通知
            if poco(**PopupElements.NOTIFICATION).exists():
                poco(**PopupElements.THINK_AGAIN).click()
                logger.info("处理消息通知：点击再想想")
                continue
                
            # 处理更新提示
            if poco(**PopupElements.UPDATE_NOW).exists():
                if poco(**PopupElements.NEXT_INSTALL).exists():
                    poco(**PopupElements.NEXT_INSTALL).click()
                    logger.info("处理更新提示：点击下次安装")
                elif poco(**PopupElements.CLOSE_UPDATE).exists():
                    poco(**PopupElements.CLOSE_UPDATE).click()
                    logger.info("处理更新提示：点击关闭")
                continue
            
            # 处理广告弹窗 - 带倒计时的跳过按钮
            if poco(**PopupElements.SKIP_AD_WITH_TIME).exists():
                element = poco(**PopupElements.SKIP_AD_WITH_TIME)
                if element.attr('clickable'):
                    element.click()
                    logger.info("处理广告：点击带倒计时的跳过按钮")
                    continue
            
            # 处理广告弹窗 - 普通跳过按钮
            if poco(**PopupElements.SKIP_AD).exists():
                poco(**PopupElements.SKIP_AD).click()
                logger.info("处理广告：点击跳过按钮")
                continue
            
            # 处理广告弹窗 - 关闭按钮
            if poco(**PopupElements.CLOSE_AD).exists():
                poco(**PopupElements.CLOSE_AD).click()
                logger.info("处理广告：点击关闭广告按钮")
                continue
            
            # 处理广告弹窗 - X按钮
            if poco(**PopupElements.CLOSE_AD_X).exists():
                poco(**PopupElements.CLOSE_AD_X).click()
                logger.info("处理广告：点击X关闭按钮")
                continue
                
        except Exception as e:
            logger.warning(f"弹窗处理异常: {e}")
        
        # 短暂休眠，避免过度消耗CPU
        sleep(WaitTime.ULTRA_SHORT)

def start_popup_handler():
    """启动弹窗处理线程"""
    global popup_handler_running, popup_handler_thread
    
    if popup_handler_thread and popup_handler_thread.is_alive():
        logger.warning("弹窗处理线程已在运行")
        return
        
    popup_handler_running = True
    popup_handler_thread = threading.Thread(
        target=handle_popups,
        name="PopupHandler",
        daemon=True
    )
    popup_handler_thread.start()
    logger.info("弹窗处理线程已启动")

def stop_popup_handler():
    """停止弹窗处理线程"""
    global popup_handler_running, popup_handler_thread
    
    if not popup_handler_thread:
        logger.warning("弹窗处理线程未启动")
        return
        
    popup_handler_running = False
    popup_handler_thread.join(timeout=1)
    popup_handler_thread = None
    logger.info("弹窗处理线程已停止")
