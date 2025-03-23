#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import threading

from moduls.android.common.app_common import *
from moduls.android.common.poco_common import poco
from moduls.android.homepage.meeting import Meeting
from moduls.android.inmeeting.morepage import Record

import threading
import time

class Test_application_init(object):

    def test_01_demo(self):

        # 创建退出事件和线程
        exit_event = threading.Event()
        thread_handle_popup = threading.Thread(target=self.handle_popup, args=(exit_event,))
        thread_handle_popup.daemon = True
        thread_handle_popup.start()

        try:
            # 执行测试流程
            open_android_app(package_name="com.tencent.wemeet.app")
            time.sleep(3)  # 等待应用启动
            Meeting().check_homepage()
            Meeting().check_meetingpage()
            Meeting().join_meeting()
            Record().record()
            Meeting().end_meeting()
            Meeting().book_meeting()
        finally:
            # 关闭应用并停止弹窗处理线程
            close_android_app(package_name="com.tencent.wemeet.app")
            exit_event.set()  # 停止弹窗处理线程
            thread_handle_popup.join(timeout=2)  # 等待线程安全退出

    def handle_popup(self, exit_event):
        single_check_timeout = 5  # 单次检测超时时间（秒）
        while not exit_event.is_set():
            start_time = time.time()  # 记录开始时间
            while (time.time() - start_time) < single_check_timeout and not exit_event.is_set():
                if poco(text='允许本次使用').exists():
                    time.sleep(3)
                    try:
                        poco(text='允许本次使用').click()
                        time.sleep(1)  # 点击后等待一段时间
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break  # 处理完弹窗后退出当前循环
                if poco(text='网络状况不佳').exists():
                    time.sleep(3)
                    try:
                        poco(text='关闭视频').click()
                        time.sleep(1)  # 点击后等待一段时间
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break
                time.sleep(0.5)  # 减少轮询频率


if __name__ == '__main__':
    Test_application_init().test_01_demo()
