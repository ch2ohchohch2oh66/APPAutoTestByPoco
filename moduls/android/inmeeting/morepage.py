#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: More page functionality

from time import sleep
from airtest.core.api import *

from moduls.android.common.base_page import BasePage
from moduls.android.common.poco_common import *
from moduls.android.common.ui_elements import InMeetingElements, WaitTime
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage

class MorePage(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = InMeetingElements()
    
    def click_more_button(self):
        """点击更多按钮"""
        logger.info('点击更多按钮')
        try:
            self.click_element(self.elements.MORE_BUTTON)
            sleep(WaitTime.ULTRA_SHORT)
            return True
        except Exception as e:
            logger.error(f"点击更多按钮失败: {e}")
            return False
    
    def click_end_meeting(self):
        """点击结束会议"""
        logger.info('点击结束会议')
        try:
            self.click_element(self.elements.END_MEETING_BUTTON)
            sleep(WaitTime.MEDIUM)
            return True
        except Exception as e:
            logger.error(f"点击结束会议失败: {e}")
            return False
    
    def click_confirm_end(self):
        """点击确认结束"""
        logger.info('点击确认结束')
        try:
            self.click_element(self.elements.CONFIRM_END_BUTTON)
            sleep(WaitTime.SHORT)
            return True
        except Exception as e:
            logger.error(f"点击确认结束失败: {e}")
            return False
    
    def end_meeting(self):
        """结束会议流程"""
        logger.info('开始结束会议')
        
        # 点击更多按钮
        if not self.click_more_button():
            return False
        
        # 点击结束会议
        if not self.click_end_meeting():
            return False
        
        # 点击确认结束
        if not self.click_confirm_end():
            return False
        
        logger.info('结束会议成功')
        return True