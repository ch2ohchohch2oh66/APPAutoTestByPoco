#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Record functionality

from time import sleep
from airtest.core.api import *

from moduls.android.common.base_page import BasePage
from moduls.android.common.poco_common import *
from configs.android.ui_elements import InMeetingElements
from configs.other_configs import WaitTime
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage

class Record(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = InMeetingElements()
        self.default_page = InmeetingDefaultpage()

    def start_record(self):
        """开启录制"""
        logger.info('开启录制')
        try:
            self.click_element(self.elements.CLOUD_RECORDING)
            if self.element_exists(self.elements.START_RECORDING):
                self.click_element(self.elements.START_RECORDING)
            assert self.element_exists(self.elements.RECORDING_STATUS)
            logger.info('开启录制成功')
            sleep(WaitTime.MEDIUM)
            return True
        except Exception as e:
            logger.error(f"开启录制失败: {e}")
            return False

    def pause_record(self):
        """暂停录制"""
        logger.info('暂停录制')
        try:
            if (self.element_exists(self.elements.RECORDING_STATUS) and 
                not self.element_exists(self.elements.PAUSE_RECORDING)):
                self.click_element(self.elements.RECORDING_STATUS)
                sleep(WaitTime.SHORT)
                self.click_element(self.elements.PAUSE_RECORDING)
                assert self.element_exists(self.elements.RECORDING_PAUSED)
                logger.info('暂停录制成功')
                sleep(WaitTime.MEDIUM)
                return True
            return False
        except Exception as e:
            logger.error(f"暂停录制失败: {e}")
            return False

    def restore_record(self):
        """恢复录制"""
        logger.info('恢复录制')
        try:
            if (self.element_exists(self.elements.RECORDING_PAUSED) and
                not self.element_exists(self.elements.RESUME_RECORDING)):
                self.click_element(self.elements.RECORDING_PAUSED)
                sleep(WaitTime.SHORT)
                self.click_element(self.elements.RESUME_RECORDING)
                assert self.element_exists(self.elements.RECORDING_STATUS)
                logger.info('恢复录制成功')
                sleep(WaitTime.MEDIUM)
                return True
            return False
        except Exception as e:
            logger.error(f"恢复录制失败: {e}")
            return False

    def stop_record(self):
        """结束录制"""
        logger.info('结束录制')
        try:
            if self.element_exists(self.elements.RECORDING_STATUS):
                self.click_element(self.elements.RECORDING_STATUS)
            elif self.element_exists(self.elements.RECORDING_PAUSED):
                self.click_element(self.elements.RECORDING_PAUSED)
            else:
                logger.info('未找到录制状态元素')
                return False
            sleep(WaitTime.SHORT)

            if self.element_exists(self.elements.STOP_RECORDING):
                self.click_element(self.elements.STOP_RECORDING)
                sleep(WaitTime.SHORT)
                self.click_element(self.elements.STOP_RECORDING_CONFIRM)
                logger.info('结束录制成功')
                sleep(WaitTime.SHORT)
                return True
            return False
        except Exception as e:
            logger.error(f"结束录制失败: {e}")
            return False

    def record(self):
        """执行完整的录制流程"""
        logger.info('开始录制流程')
        
        # 点击更多按钮
        if not self.default_page.click_more_button():
            return False
            
        # 开始录制
        if not self.start_record():
            return False
            
        # 暂停录制
        if not self.pause_record():
            return False
            
        # 恢复录制
        if not self.restore_record():
            return False
            
        # 停止录制
        if not self.stop_record():
            return False
            
        logger.info('录制流程完成')
        return True 