#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import logging
from moduls.android.common.app_common import *
from moduls.android.homepage.meeting import Meeting

# logger = logging.getLogger(__name__)

class Test_application_init(object):

    def test_01_open_app(self):
        open_android_app(package_name="com.tencent.wemeet.app")
        sleep(3)
        Meeting().check_homepage()
        Meeting().check_meetingpage()
        Meeting().join_meeting()
        close_android_app(package_name="com.tencent.wemeet.app")

if __name__ == '__main__':
    Test_application_init().test_01_open_app()
