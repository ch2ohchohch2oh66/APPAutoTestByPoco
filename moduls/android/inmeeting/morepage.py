#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from time import sleep
from moduls.android.common.base_page import BasePage
from moduls.android.common.ui_elements import InMeetingElements, Timeouts
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage
from moduls.android.common.poco_common import *

class Record(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = InMeetingElements()

    def start_record(self):
        """开启录制"""
        logger.info('开启录制')
        self.click_element(self.elements.CLOUD_RECORDING)
        if self.element_exists(self.elements.START_RECORDING):
            self.click_element(self.elements.START_RECORDING)
        logger.info('开启录制成功')

    def pause_record(self):
        """暂停录制"""
        logger.info('暂停录制')
        if (self.element_exists(self.elements.RECORDING_STATUS) and 
            not self.element_exists(self.elements.PAUSE_RECORDING)):
            self.click_element(self.elements.RECORDING_STATUS)
            self.click_element(self.elements.PAUSE_RECORDING)
        logger.info('暂停录制成功')

    def restore_record(self):
        """恢复录制"""
        logger.info('恢复录制')
        if self.element_exists(self.elements.RECORDING_PAUSED):
            self.click_element(self.elements.RECORDING_PAUSED)
            self.click_element(self.elements.RESUME_RECORDING)
        logger.info('恢复录制成功')

    def stop_record(self):
        """结束录制"""
        logger.info('结束录制')
        if self.element_exists(self.elements.RECORDING_STATUS):
            self.click_element(self.elements.RECORDING_STATUS)
            self.click_element(self.elements.STOP_RECORDING)
            self.click_element(self.elements.STOP_RECORDING_CONFIRM)
        logger.info('结束录制成功')

    def record(self):
        """执行完整的录制流程"""
        InmeetingDefaultpage().click_more_button()
        sleep(1)
        self.start_record()
        sleep(5)
        self.pause_record()
        sleep(5)
        self.restore_record()
        sleep(5)
        self.stop_record()