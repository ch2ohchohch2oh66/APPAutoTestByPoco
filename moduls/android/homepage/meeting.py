#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish
import os.path
from time import sleep
from airtest.core.api import *
from moduls.android.common.poco_common import *
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage

# 获取项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)
# 图片路径配置
TEMPLATE_PATHS = {
    'meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'homepage', 'meeting'),
    'book_meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'book_meeting')
}
FIND_TIMEOUT = 3  # 超时时间

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
        sleep(1)
        poco(text='开启视频').click()
        sleep(1)

    def end_meeting(self):

        logger.info('结束会议')
        InmeetingDefaultpage().call_top_and_bottom_button()
        poco(text='结束').click(sleep_interval=1)
        sleep(1)
        poco(text='结束会议').click()
        sleep(1)
        poco(textMatches='^我知道了.*$').click()
        sleep(1)
        logger.info('结束会议成功')

    def book_meeting(self):
        logger.info('预定会议')
        touch(Template(os.path.join(PROJECT_ROOT, TEMPLATE_PATHS['meeting_image_path'], 'book_meeting.png'), ST.THRESHOLD, ST.FIND_TIMEOUT))
        sleep(1)
        touch(Template(os.path.join(PROJECT_ROOT, TEMPLATE_PATHS['book_meeting_image_path'], 'next_step.png'), ST.THRESHOLD, ST.FIND_TIMEOUT))
        sleep(2)
        poco(text='开始时间').click()
        sleep(1)
        poco.swipe((0.6, 0.8), (0.6, 0.75))
        sleep(1)
        poco(desc='确定').click()
        sleep(1)
        poco(text='完成').click()
        sleep(1)
        if poco(text='会议冲突提示').exists():
            poco(text='仍然预定').click()
            sleep(1)

        poco(text='取消').click()
        sleep(1)
        poco(desc='返回').click()
        logger.info('预定会议成功')
        sleep(1)