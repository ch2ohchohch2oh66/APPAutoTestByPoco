#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish

import os.path
from time import sleep
from airtest.core.api import *
from moduls.android.common.poco_common import *
from moduls.android.common.base_page import BasePage
from moduls.android.common.ui_elements import HomePageElements, InMeetingElements, Timeouts
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage

# 获取项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)
# 图片路径配置
TEMPLATE_PATHS = {
    'meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'homepage', 'meeting'),
    'book_meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'book_meeting')
}

class Meeting(BasePage):
    def __init__(self):
        super().__init__()
        self.home_page_elements = HomePageElements()
        self.in_meeting_elements = InMeetingElements()

    def check_homepage(self):
        """检查首页元素是否存在"""
        logger.info('检查首页')
        assert self.element_exists(self.home_page_elements.MEETING_TAB), '未找到"会议"'
        assert self.element_exists(self.home_page_elements.CONTACTS_TAB), '未找到"通讯录"'
        assert self.element_exists(self.home_page_elements.PROFILE_TAB), '未找到"我的"'

    def check_meetingpage(self):
        """检查会议页面元素是否存在"""
        logger.info('检查会议页面')
        assert self.element_exists(self.home_page_elements.JOIN_MEETING), '未找到"加入会议"'
        assert self.element_exists(self.home_page_elements.QUICK_MEETING), '未找到"快速会议"'
        assert self.element_exists(self.home_page_elements.BOOK_MEETING), '未找到"预定会议"'
        assert self.element_exists(self.home_page_elements.SHARE_SCREEN), '未找到"共享屏幕"'

    def join_meeting(self, meeting_number='8104536077'):
        """加入会议"""
        logger.info('加入会议')
        self.click_element(self.home_page_elements.JOIN_MEETING)
        self.click_element(self.home_page_elements.MEETING_NUMBER_INPUT)
        self.set_element_text(self.home_page_elements.MEETING_NUMBER_INPUT, meeting_number)
        sleep(1)
        
        # 返回一次以退出输入法应用
        if poco(name='com.sohu.inputmethod.sogou:id/aut').exists():
            logger.info('退出输入法应用')
            keyevent('BACK')
            sleep(1)
            
        self.click_element(self.home_page_elements.JOIN_BUTTON)
        self.wait_for_element(self.home_page_elements.END_MEETING, Timeouts.LONG_WAIT)
        assert self.element_exists(self.home_page_elements.END_MEETING), '未找到"结束",加入会议失败'
        logger.info('加入会议成功')
        self.click_element(self.home_page_elements.TURN_ON_VIDEO)

    def end_meeting(self):
        """结束会议"""
        logger.info('结束会议')
        InmeetingDefaultpage().call_top_and_bottom_button()
        self.click_element(self.home_page_elements.END_MEETING)
        self.click_element(self.in_meeting_elements.END_MEETING_CONFIRM)
        self.click_element(self.in_meeting_elements.END_MEETING_ACKNOWLEDGE)
        logger.info('结束会议成功')

    def book_meeting(self):
        """预定会议"""
        logger.info('预定会议')
        before_book_number = poco(typeMatches='.*RecyclerView').children().__len__()
        logger.info('预定前会议数量：{}'.format(before_book_number))
        
        sleep(5)
        touch(Template(os.path.join(PROJECT_ROOT, TEMPLATE_PATHS['meeting_image_path'], 'book_meeting.jpg'), 
                      ST.THRESHOLD, ST.FIND_TIMEOUT))
        sleep(5)
        touch(Template(os.path.join(PROJECT_ROOT, TEMPLATE_PATHS['book_meeting_image_path'], 'next_step.jpg'), 
                      ST.THRESHOLD, ST.FIND_TIMEOUT))
        
        sleep(3)
        self.click_element({'text': '开始时间'})
        poco.swipe((0.6, 0.8), (0.6, 0.75), duration=0.5)
        sleep(1)
        self.click_element({'desc': '确定'})
        self.click_element({'text': '完成'})
        
        if self.element_exists({'text': '会议冲突提示'}):
            self.click_element({'text': '仍然预定'})

        self.click_element({'text': '取消'})
        self.click_element({'desc': '返回'})
        
        after_book_number = poco(typeMatches='.*RecyclerView').offspring(nameMatches='.*ViewGroup$').__len__()
        logger.info('预定后会议数量：{}'.format(after_book_number))
        assert after_book_number > before_book_number, '预定会议失败'
        logger.info('预定会议成功')
        sleep(3)
