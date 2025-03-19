# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish
from airtest.core.api import auto_setup, wake
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__, devices=["android:///?ime_method=ADBIME"])
wake()
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False, force_restart=True)