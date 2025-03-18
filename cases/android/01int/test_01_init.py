#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import logging
from moduls.android.app.app_common import *

logger = logging.getLogger(__name__)

class Test_application_init(object):

    def test_01_open_app(self):
        open_android_app(package_name="com.tencent.wemeet.app")