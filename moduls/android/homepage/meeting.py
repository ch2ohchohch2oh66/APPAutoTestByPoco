#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish
from time import sleep

from airtest.core.api import auto_setup, keyevent
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__, devices=["android:///?ime_method=ADBIME"])
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, force_restart=True)
# print(G.DEVICE)

class Meeting:
    # def __init__(self, meeting_name, meeting_time, meeting_location, meeting_description):
    #     self.meeting_name = meeting_name
    #     self.meeting_time = meeting_time
    #     self.meeting_location = meeting_location
    #     self.meeting_description = meeting_description
    #
    # def get_meeting_name(self):
    #     return self.meeting_name
    #
    # def get_meeting_time(self):
    #     return self.meeting_time
    #
    # def get_meeting_location(self):
    #     pass

    def join_meeting(self):
        assert poco(text='加入会议').exists(), '未找到会议页面'
        poco(text='加入会议').click()
        sleep(1)
        poco(text='请输入会议号').click()
        sleep(1)
        poco(text='请输入会议号').set_text('4279512998')
        sleep(1)
        # 返回一次以退出输入法应用
        keyevent('BACK')
        # poco(name='com.tencent.wemeet.app:id/ali').click()
        sleep(1)
        poco(name='com.tencent.wemeet.app:id/xb').click()
        sleep(5)
