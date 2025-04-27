#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import time
import logging

from moduls.android.common.app_common import *
from configs.other_configs import WaitTime, APP_PACKAGE
from moduls.android.homepage.meeting import Meeting
from moduls.android.inmeeting.record import Record
from moduls.android.homepage.book_meeting import BookMeeting
from cases.android.common.test_base import TestBase

logger = logging.getLogger(__name__)

class Test_application_init(TestBase):
    """应用初始化测试"""

    def test_01_demo(self):
        """测试主流程"""
        try:
            # 执行测试流程
            open_android_app(APP_PACKAGE['tencent_meeting'])
            time.sleep(WaitTime.MEDIUM)  # 等待应用启动
            Meeting().check_homepage()
            Meeting().check_meetingpage()
            Meeting().join_meeting()
            Record().record()
            Meeting().end_meeting()
            BookMeeting().book_meeting()
        finally:
            # 关闭应用
            close_android_app(APP_PACKAGE['tencent_meeting'])


if __name__ == '__main__':
    Test_application_init().test_01_demo()
