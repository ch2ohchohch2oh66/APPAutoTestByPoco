#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish

from time import sleep
from airtest.core.api import keyevent
from utils.wrap_poco import *
# import logging
#
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)


class Meeting:

    def check_homepage(self):
        logger.info('检查首页')
        assert poco(nameMatches='.*id/act$', textMatches='.*会议.*').exists(), '未找到“会议”'
        assert poco(nameMatches='.*id/act$', textMatches='.*通讯录.*').exists(), '未找到“通讯录”'
        assert poco(nameMatches='.*id/act$', textMatches='.*我的.*').exists(), '未找到“我的”'

    def check_meetingpage(self):
        logger.info('检查会议页面')
        assert poco(text='加入会议').exists(), '未找到“加入会议”'
        assert poco(text='快速会议').exists(), '未找到“快速会议”'
        assert poco(text='预定会议').exists(), '未找到“预定会议”'
        assert poco(text='共享屏幕').exists(), '未找到“共享屏幕”'

    def join_meeting(self):
        logger.info('加入会议')
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
        logger.info('加入会议成功')
        sleep(5)
        logger.info('结束会议')
        poco(name='com.tencent.wemeet.app:id/dq').click()
        sleep(1)
        poco(text='结束会议').click()
        sleep(1)
        poco(textMatches='^我知道了.*$').click()
        sleep(1)
        logger.info('结束会议成功')
