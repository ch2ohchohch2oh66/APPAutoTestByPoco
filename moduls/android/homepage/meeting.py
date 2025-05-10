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
from configs.android.ui_elements import HomePageElements, InMeetingElements
from configs.android.other_configs import WaitTime
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage
from utils.config_reader import ConfigReader

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
        assert self.wait_element_exists(self.home_page_elements.MEETING_TAB), '未找到"会议"'
        assert self.wait_element_exists(self.home_page_elements.CONTACTS_TAB), '未找到"通讯录"'
        assert self.wait_element_exists(self.home_page_elements.PROFILE_TAB), '未找到"我的"'

    def check_meetingpage(self):
        """检查会议页面元素是否存在"""
        logger.info('检查会议页面')
        assert self.wait_element_exists(self.home_page_elements.MEETING_TAB), '未找到"会议"'
        assert self.wait_element_exists(self.home_page_elements.JOIN_MEETING), '未找到"加入会议"'
        assert self.wait_element_exists(self.home_page_elements.QUICK_MEETING), '未找到"快速会议"'
        assert self.wait_element_exists(self.home_page_elements.BOOK_MEETING), '未找到"预定会议"'
        assert self.wait_element_exists(self.home_page_elements.SHARE_SCREEN), '未找到"共享屏幕"'

    def join_meeting(self, meeting_number=None):
        """加入会议"""
        logger.info('加入会议')
        
        # 如果未指定会议号，从配置文件获取
        if meeting_number is None:
            meeting_number = ConfigReader.get_meeting_number()
            logger.info(f'从配置文件获取会议号: {meeting_number}')
        
        self.click_element(self.home_page_elements.JOIN_MEETING)
        self.click_element(self.home_page_elements.MEETING_NUMBER_INPUT)
        self.set_element_text(self.home_page_elements.MEETING_NUMBER_INPUT, meeting_number)
        sleep(WaitTime.ULTRA_SHORT)
        
        # 返回一次以退出输入法应用
        # if poco(name='com.sohu.inputmethod.sogou:id/aut').exists():
        #     logger.info('退出输入法应用')
        #     keyevent('BACK')
        #     sleep(WaitTime.ULTRA_SHORT)
            
        self.click_element(self.home_page_elements.JOIN_BUTTON)
        self.wait_for_element(self.in_meeting_elements.END_MEETING, WaitTime.MEDIUM)
        assert self.wait_element_exists(self.in_meeting_elements.END_MEETING), '未找到"结束",加入会议失败'
        logger.info('加入会议成功')
        self.click_element(self.in_meeting_elements.TURN_ON_VIDEO)

    def end_meeting(self):
        """结束会议"""
        logger.info('结束会议')
        InmeetingDefaultpage().call_top_and_bottom_button()
        self.click_element(self.in_meeting_elements.END_MEETING)
        self.click_element(self.in_meeting_elements.END_MEETING_CONFIRM)
        self.click_existed_element(self.in_meeting_elements.END_MEETING_ACKNOWLEDGE)
        logger.info('结束会议成功')

    def is_on_home_page(self):
        """检查是否在首页"""
        logger.info('检查是否在首页')
        if self.wait_element_exists(self.home_page_elements.MEETING_TAB):
            logger.info('在首页')
            return True
        else:
            logger.info('不在首页')
            return False
