#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 会议外检查测试

import pytest
import logging
from time import sleep

from configs.android.other_configs import WaitTime
from moduls.android.homepage.meeting import Meeting

logger = logging.getLogger(__name__)

class Test_OutMeeting_Check:
    """会议外检查测试"""

    def test_01_homepage_check(self):
        """测试首页元素检查"""
        logger.info("开始首页元素检查")
        Meeting().check_homepage()
        sleep(WaitTime.SHORT)
        
    def test_02_meetingpage_check(self):
        """测试会议页面元素检查"""
        logger.info("开始会议页面元素检查")
        Meeting().check_meetingpage()
        sleep(WaitTime.SHORT) 