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

    def test_01_open_app(self):
        open_android_app(package_name="com.tencent.wemeet.app")
        time.sleep(3)  # 等待应用启动

        # 创建退出事件和线程
        exit_event = threading.Event()
        thread_pop_up_window = threading.Thread(target=self.pop_up_window, args=(exit_event,))
        thread_pop_up_window.daemon = True
        thread_pop_up_window.start()

        try:
            # 执行测试流程
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
            thread_pop_up_window.join(timeout=2)  # 等待线程安全退出

    def pop_up_window(self, exit_event):
        single_check_timeout = 5  # 单次检测超时时间（秒）
        while not exit_event.is_set():
            start_time = time.time()  # 记录开始时间
            while (time.time() - start_time) < single_check_timeout and not exit_event.is_set():
                if poco(text='允许本次使用').exists():
                    try:
                        poco(text='允许本次使用').click()
                        time.sleep(1)  # 点击后等待一段时间
                    except Exception as e:
                        print(f"Failed to handle popup: {e}")
                    break  # 处理完弹窗后退出当前循环
                time.sleep(0.5)  # 减少轮询频率


if __name__ == '__main__':
    Test_application_init().test_01_open_app()
