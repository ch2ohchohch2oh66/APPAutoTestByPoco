#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from moduls.android.common.base_page import BasePage
from moduls.android.common.ui_elements import InMeetingElements, WaitTime
from moduls.android.common.poco_common import *
from time import sleep
from airtest.core.api import *

class InmeetingDefaultpage(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = InMeetingElements()

    def call_top_and_bottom_button(self):
        """显示顶部和底部按钮"""
        if not self.element_exists(self.elements.MORE_BUTTON):
            poco.click([0.5, 0.5])

    def click_more_button(self):
        """点击更多按钮"""
        logger.info('点击更多按钮')
        if not self.element_exists(self.elements.MORE_BUTTON):
            logger.info('更多按钮不存在，点击屏幕中间')
            poco.click([0.5, 0.5])
        # self.wait_for_element(self.elements.MORE_BUTTON)
        self.click_element(self.elements.MORE_BUTTON)
        return True

    # def click_join_button(self):
    #     """点击加入按钮"""
    #     logger.info('点击加入按钮')
    #     try:
    #         self.click_element(self.elements.JOIN_BUTTON)
    #         sleep(WaitTime.MEDIUM)
    #         return True
    #     except Exception as e:
    #         logger.error(f"点击加入按钮失败: {e}")
    #         return False
    
    def click_leave_button(self):
        """点击离开按钮"""
        logger.info('点击离开按钮')
        try:
            self.click_element(self.elements.END_MEETING)
            sleep(WaitTime.MEDIUM)
            return True
        except Exception as e:
            logger.error(f"点击离开按钮失败: {e}")
            return False
    
    def click_confirm_leave(self):
        """点击确认离开"""
        logger.info('点击确认离开')
        try:
            self.click_element(self.elements.END_MEETING_CONFIRM)
            sleep(WaitTime.SHORT)
            return True
        except Exception as e:
            logger.error(f"点击确认离开失败: {e}")
            return False
    
    # def join_meeting(self):
    #     """加入会议流程"""
    #     logger.info('开始加入会议')
    #
    #     # 点击加入按钮
    #     if not self.click_join_button():
    #         return False
    #
    #     logger.info('加入会议成功')
    #     return True
    
    def leave_meeting(self):
        """离开会议流程"""
        logger.info('开始离开会议')
        
        # 点击离开按钮
        if not self.click_leave_button():
            return False
        
        # 点击确认离开
        if not self.click_confirm_leave():
            return False
        
        logger.info('离开会议成功')
        return True