#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import threading
import time

from moduls.android.common.app_common import *
from moduls.android.common.poco_common import poco
from configs.android.ui_elements import PopupElements
from configs.other_configs import WaitTime, APP_PACKAGE
from moduls.android.homepage.meeting import Meeting
from moduls.android.inmeeting.record import Record
from moduls.android.homepage.book_meeting import BookMeeting

class Test_application_init(object):

    def test_01_demo(self):
        # 创建退出事件和线程
        exit_event = threading.Event()
        thread_handle_popup = threading.Thread(target=self.handle_popup, args=(exit_event,))
        thread_handle_popup.daemon = True
        thread_handle_popup.start()

        try:
            # 执行测试流程
            open_android_app(APP_PACKAGE['tencent_meeting'])
            time.sleep(WaitTime.MEDIUM)  # 等待应用启动
            Meeting().check_homepage()
            Meeting().check_meetingpage()
            Meeting().join_meeting()
            Record().record()
            Meeting().end_meeting()
            BookMeeting().book_meeting()
        finally:
            # 关闭应用并停止弹窗处理线程
            close_android_app(APP_PACKAGE['tencent_meeting'])
            exit_event.set()  # 停止弹窗处理线程
            thread_handle_popup.join(timeout=WaitTime.MEDIUM)  # 等待线程安全退出

    def handle_popup(self, exit_event):
        while not exit_event.is_set():
            start_time = time.time()  # 记录开始时间
            while (time.time() - start_time) < WaitTime.MEDIUM and not exit_event.is_set():
                if poco(**PopupElements.ALLOW_ONCE).exists():
                    try:
                        poco(**PopupElements.ALLOW_ONCE).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break  # 处理完弹窗后退出当前循环
                if poco(**PopupElements.POOR_NETWORK).exists():
                    try:
                        poco(**PopupElements.CLOSE_VIDEO).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break
                if poco(**PopupElements.NOTIFICATION).exists():
                    try:
                        poco(**PopupElements.THINK_AGAIN).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break
                if poco(**PopupElements.NEXT_INSTALL).exists():
                    try:
                        poco(**PopupElements.NEXT_INSTALL).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break
                if poco(**PopupElements.UPDATE_NOW).exists():
                    try:
                        poco(**PopupElements.CLOSE_UPDATE).click()
                        time.sleep(WaitTime.ULTRA_SHORT)  
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break
                time.sleep(WaitTime.ULTRA_SHORT)  # 减少轮询频率


if __name__ == '__main__':
    Test_application_init().test_01_demo()
