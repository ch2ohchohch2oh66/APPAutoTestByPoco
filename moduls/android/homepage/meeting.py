#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish

from time import sleep
from airtest.core.api import keyevent
from utils.wrap_poco import *

class Meeting:


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
        poco(name='com.tencent.wemeet.app:id/dq').click()
        sleep(1)
        # poco(name='com.tencent.wemeet.app:id/dq').click()
        sleep(1)
        poco(text='结束会议').click()
        sleep(1)
        poco(textMatches='^我知道了.*$').click()
        sleep(1)

