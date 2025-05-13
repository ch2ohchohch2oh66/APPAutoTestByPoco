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
from configs.android.other_configs import WaitTime
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
            if not self.element_exists(self.elements.CLOUD_RECORDING):
                logger.info('云录制按钮不存在，点击"更多"按钮')
                self.default_page.click_more_button()
            self.click_element(self.elements.CLOUD_RECORDING)
            assert self.wait_element_exists(self.elements.START_RECORDING)
            assert self.click_element(self.elements.START_RECORDING), '点击开始录制失败'
            assert self.wait_element_exists(self.elements.RECORDING_STATUS)
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
                assert self.click_element(self.elements.RECORDING_STATUS)
                sleep(WaitTime.SHORT)
                assert self.click_element(self.elements.PAUSE_RECORDING)
                assert self.wait_element_exists(self.elements.RECORDING_PAUSED)
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
                assert self.click_element(self.elements.RECORDING_PAUSED)
                sleep(WaitTime.SHORT)
                assert self.click_element(self.elements.RESUME_RECORDING)
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
                assert self.click_element(self.elements.RECORDING_STATUS)
            elif self.element_exists(self.elements.RECORDING_PAUSED):
                assert self.click_element(self.elements.RECORDING_PAUSED)
            else:
                logger.info('未找到录制状态元素')
                return False
            sleep(WaitTime.SHORT)

            if self.element_exists(self.elements.STOP_RECORDING):
                assert self.click_element(self.elements.STOP_RECORDING)
                sleep(WaitTime.SHORT)
                assert self.click_element(self.elements.STOP_RECORDING_CONFIRM)
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
        assert self.default_page.click_more_button()
            
        # 开始录制
        assert self.start_record()
            
        # 暂停录制
        assert self.pause_record()
            
        # 恢复录制
        assert self.restore_record()
            
        # 停止录制
        assert self.stop_record()
            
        logger.info('录制流程完成')