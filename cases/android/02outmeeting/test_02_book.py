#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 预约会议测试

import pytest
import logging
from time import sleep

from configs.android.other_configs import WaitTime
from moduls.android.homepage.book_meeting import BookMeeting

logger = logging.getLogger(__name__)

class Test_OutMeeting_Book:
    """预约会议测试"""

    def test_01_book_meeting(self):
        """测试预约会议流程"""
        logger.info("开始预约会议测试")
        BookMeeting().book_meeting()
        sleep(WaitTime.SHORT) 