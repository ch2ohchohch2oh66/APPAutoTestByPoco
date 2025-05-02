#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 会议中录制测试

import pytest
import logging
from time import sleep

from configs.android.other_configs import WaitTime
from moduls.android.common.app_common import open_android_app
from moduls.android.homepage.meeting import Meeting
from moduls.android.inmeeting.record import Record

logger = logging.getLogger(__name__)

class Test_InMeeting_Record:
    """会议中录制测试"""
    def setup_class(self):
        """测试类开始前检查是否在HomePage, 如果不在则重启APP以返回HomePage"""
        logger.info("检查是否在HomePage...")
        if not Meeting().is_on_home_page():
            logger.info("不在HomePage，重启APP...")
            open_android_app()
            sleep(WaitTime.MEDIUM)

    def setup_method(self):
        """每个测试方法前加入会议"""
        logger.info("加入会议...")
        Meeting().join_meeting()
        sleep(WaitTime.SHORT)

    def teardown_method(self):
        """每个测试方法后结束会议"""
        logger.info("结束会议...")
        Meeting().end_meeting()
        sleep(WaitTime.SHORT)

    def test_01_record(self):
        """测试会议录制流程"""
        logger.info("开始会议录制测试")
        Record().record()
        sleep(WaitTime.SHORT) 