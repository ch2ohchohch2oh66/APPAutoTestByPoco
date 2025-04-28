#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: Keep Hungry Keep Foolish

import threading
import time
import logging

from moduls.android.common.poco_common import poco
from configs.android.ui_elements import PopupElements
from configs.android.other_configs import WaitTime

logger = logging.getLogger(__name__)

class PopupHandler:
    """弹窗处理器类，用于自动处理应用中出现的各种弹窗"""
    
    def __init__(self):
        """初始化弹窗处理器"""
        self.exit_event = threading.Event()
        self.thread = None
    
    def start(self):
        """启动弹窗处理线程"""
        if self.thread is not None and self.thread.is_alive():
            logger.warning("弹窗处理线程已经在运行")
            return
            
        self.exit_event.clear()
        self.thread = threading.Thread(target=self._handle_popup_thread)
        self.thread.daemon = True
        self.thread.start()
        logger.info("弹窗处理守护线程已启动")
        
    def stop(self, timeout=WaitTime.MEDIUM):
        """停止弹窗处理线程"""
        if self.thread is None or not self.thread.is_alive():
            logger.warning("弹窗处理线程未运行")
            return
            
        logger.info("正在停止弹窗处理守护线程...")
        self.exit_event.set()
        self.thread.join(timeout=timeout)
        logger.info("弹窗处理守护线程已停止")
    
    def _handle_popup_thread(self):
        """弹窗处理线程的主函数"""
        logger.info("弹窗处理线程开始运行")
        
        while not self.exit_event.is_set():
            start_time = time.time()  # 记录开始时间
            
            # 检查和处理各种弹窗，超过中等等待时间后重新开始检查循环
            while (time.time() - start_time) < WaitTime.MEDIUM and not self.exit_event.is_set():
                # 权限请求弹窗
                if poco(**PopupElements.ALLOW_ONCE).exists():
                    try:
                        logger.info('检测到权限请求弹窗，点击"允许本次使用"')
                        poco(**PopupElements.ALLOW_ONCE).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        logger.error(f"处理权限请求弹窗失败: {e}")
                    break  # 处理完弹窗后退出当前循环
                
                # 网络状况不佳弹窗
                if poco(**PopupElements.POOR_NETWORK).exists():
                    try:
                        logger.info('检测到网络状况不佳弹窗，点击"关闭视频"')
                        poco(**PopupElements.CLOSE_VIDEO).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        logger.error(f"处理网络状况不佳弹窗失败: {e}")
                    break
                
                # 消息通知弹窗
                if poco(**PopupElements.NOTIFICATION).exists():
                    try:
                        logger.info('检测到消息通知弹窗，点击"再想想"')
                        poco(**PopupElements.THINK_AGAIN).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        logger.error(f"处理消息通知弹窗失败: {e}")
                    break
                
                # 安装提示弹窗
                if poco(**PopupElements.NEXT_INSTALL).exists():
                    try:
                        logger.info('检测到安装提示弹窗，点击"下次安装"')
                        poco(**PopupElements.NEXT_INSTALL).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        logger.error(f"处理安装提示弹窗失败: {e}")
                    break
                
                # 更新提示弹窗
                if poco(**PopupElements.UPDATE_NOW).exists():
                    try:
                        logger.info('检测到更新提示弹窗，点击关闭按钮')
                        poco(**PopupElements.CLOSE_UPDATE).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        logger.error(f"处理更新提示弹窗失败: {e}")
                    break
                
                # 短暂休眠，减少轮询频率
                time.sleep(WaitTime.ULTRA_SHORT)
        
        logger.info("弹窗处理线程已退出")


# 创建全局单例实例
popup_handler = PopupHandler()


def start_popup_handler():
    """启动弹窗处理器"""
    popup_handler.start()
    
    
def stop_popup_handler(timeout=WaitTime.MEDIUM):
    """停止弹窗处理器"""
    popup_handler.stop(timeout=timeout)


if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()  # 输出到控制台
        ]
    )
    
    # 测试弹窗处理
    start_popup_handler()
    
    try:
        # 模拟主程序运行
        print("主程序正在运行...")
        time.sleep(60)  # 运行60秒
    finally:
        # 停止弹窗处理
        stop_popup_handler()
        print("程序退出")
