#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Book meeting functionality

import os.path
from time import sleep
from airtest.core.api import *

from moduls.android.common.base_page import BasePage
from moduls.android.common.poco_common import *
from configs.android.ui_elements import BookMeetingElements
from configs.android.other_configs import WaitTime, IMAGE_PATHS, IMAGE_FILES

logger = logging.getLogger(__name__)

class BookMeeting(BasePage):
    """预约会议页面"""
    
    def __init__(self):
        super().__init__()
        self.elements = BookMeetingElements()
    
    def get_meeting_count(self):
        """获取当前会议列表中的会议数量"""
        if self.element_exists(self.elements.MEETING_LIST):
            return self.poco(**self.elements.MEETING_LIST).children().__len__()
        return 0
    
    def get_meeting_items_count(self):
        """获取会议列表项目数量"""
        if self.element_exists(self.elements.MEETING_LIST):
            return self.poco(**self.elements.MEETING_LIST).offspring(**self.elements.MEETING_LIST_ITEMS).__len__()
        return 0
    
    def click_book_meeting_icon(self):
        """点击预定会议图标"""
        logger.info('点击预定会议图标')
        try:
            touch(Template(os.path.join(IMAGE_PATHS['meeting_image_path'], IMAGE_FILES['book_meeting']), 
                          ST.THRESHOLD, ST.FIND_TIMEOUT))
            return True
        except Exception as e:
            logger.error(f"点击预定会议图标失败: {e}")
            return False
             
    def click_next_step(self):
        """点击下一步按钮"""
        logger.info('点击下一步按钮')
        try:
            if self.element_exists(self.elements.NEXT_STEP_BUTTON):
                self.click_element(self.elements.NEXT_STEP_BUTTON)
                return True
            else:
                touch(Template(os.path.join(IMAGE_PATHS['book_meeting_image_path'], IMAGE_FILES['next_step']), 
                              ST.THRESHOLD, ST.FIND_TIMEOUT))
                return True
        except Exception as e:
            logger.error(f"点击下一步按钮失败: {e}")
            return False
             
    def set_meeting_time(self):
        """设置会议时间"""
        logger.info('设置会议时间')
        self.click_element(self.elements.START_TIME)
        sleep(WaitTime.SHORT)
        
        # 使用封装的滑动方法
        start_point = self.elements.TIME_PICKER_START_POINT
        end_point = self.elements.TIME_PICKER_END_POINT
        duration = self.elements.TIME_PICKER_DURATION
        
        poco.swipe(start_point, end_point, duration=duration)
        sleep(WaitTime.SHORT)

        self.click_element(self.elements.CONFIRM_BUTTON)
        sleep(WaitTime.SHORT)
    
    def click_complete(self):
        """点击完成按钮并处理可能的时间冲突"""
        logger.info('点击完成按钮')
        self.click_element(self.elements.COMPLETE_BUTTON)
        sleep(WaitTime.MEDIUM)
        
        # 检查并处理时间冲突
        logger.info('检查时间冲突')
        if self.element_exists(self.elements.CONFLICT_PROMPT):
            logger.info('检测到时间冲突提示')
            self.click_element(self.elements.BOOK_ANYWAY_BUTTON)
            sleep(WaitTime.SHORT)
        logger.info('未检测到时间冲突提示')
    
    # def handle_meeting_conflict(self):
    #     """处理会议冲突提示"""
    #     if self.element_exists(self.elements.CONFLICT_PROMPT):
    #         logger.info('处理会议冲突提示')
    #         self.click_element(self.elements.BOOK_ANYWAY_BUTTON)
    #         return True
    #     return False
    
    def cancel_and_return(self):
        """取消并返回"""
        logger.info('取消并返回')
        self.click_element(self.elements.CANCEL_BUTTON)
        self.click_element(self.elements.BACK_BUTTON)
    
    def book_meeting(self):
        """预定会议流程"""
        logger.info('开始预定会议')
        
        # 获取预定前会议数量
        before_book_number = self.get_meeting_count()
        logger.info('预定前会议数量：{}'.format(before_book_number))
        
        # 点击预定会议图标
        self.click_book_meeting_icon()
        sleep(WaitTime.MEDIUM)
        
        # 点击下一步
        self.click_next_step()
        sleep(WaitTime.MEDIUM)
        
        # 设置会议时间
        self.set_meeting_time()
        sleep(WaitTime.SHORT)
        
        # 点击完成并处理可能的时间冲突
        self.click_complete()
        sleep(WaitTime.SHORT)
        
        # 取消并返回
        self.cancel_and_return()
        sleep(WaitTime.MEDIUM)
        
        # 获取预定后会议数量
        after_book_number = self.get_meeting_items_count()
        logger.info('预定后会议数量：{}'.format(after_book_number))
        
        # 验证预定是否成功
        assert after_book_number > before_book_number, '预定会议失败'
        logger.info('预定会议成功')
        
        return True 