# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish
from airtest.core.api import auto_setup, wake, connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


auto_setup(__file__, devices=["android:///?ime_method=ADBIME"])
# device = connect_device("android:///?ime_method=ADBIME")
wake()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, force_restart=True)