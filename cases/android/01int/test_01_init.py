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

class Test_application_init(object):

    def test_01_open_app(self):
        open_android_app(package_name="com.tencent.wemeet.app")
        sleep(3)
        exit_event = threading.Event()
        thread_pop_up_window = threading.Thread(target=self.pop_up_window, args=(exit_event,))
        thread_pop_up_window.setDaemon(True)
        thread_pop_up_window.start()

        Meeting().check_homepage()
        Meeting().check_meetingpage()
        Meeting().join_meeting()
        Record().record()
        Meeting().end_meeting()
        Meeting().book_meeting()
        close_android_app(package_name="com.tencent.wemeet.app")
        exit_event.set()
    def pop_up_window(self, exit_event):
        while not exit_event.is_set():
            exit_event.wait(1)
            if poco(text='允许本次使用').exists():
                poco(text='允许本次使用').click()
                sleep(1)

if __name__ == '__main__':
    Test_application_init().test_01_open_app()
