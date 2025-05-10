#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from poco.exceptions import PocoTargetTimeout, PocoNoSuchNodeException
from moduls.android.common.base_page import BasePage
from configs.android.ui_elements import InMeetingElements
from moduls.android.common.poco_common import *
from configs.android.other_configs import WaitTime, MAX_RETRY
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
        retry_count = 0
        max_retries = MAX_RETRY
        while retry_count < max_retries:
            try:
                if not self.element_exists(self.elements.MORE_BUTTON):
                    logger.info('更多按钮不存在，点击屏幕中间')
                    poco.click([0.5, 0.5])
                self.click_element(self.elements.MORE_BUTTON)
                return True
            except (PocoTargetTimeout, PocoNoSuchNodeException) as e:
                retry_count += 1
                logger.error(f'点击更多按钮失败: {e}')
                logger.info(f'重试中: ({retry_count}/{max_retries})')
        logger.error('点击更多按钮失败，已达到最大重试次数')
        return False
    
    def click_leave_button(self):
        """点击离开按钮"""
        logger.info('点击离开按钮')
        try:
            self.click_element(self.elements.END_MEETING)
            sleep(WaitTime.MEDIUM)
            return True
        except Exception as e:
            logger.error(f'点击离开按钮失败: {e}')
            return False
    
    def click_confirm_leave(self):
        """点击确认离开"""
        logger.info('点击确认离开')
        try:
            self.click_element(self.elements.END_MEETING_CONFIRM)
            sleep(WaitTime.SHORT)
            return True
        except Exception as e:
            logger.error(f'点击确认离开失败: {e}')
            return False
    
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