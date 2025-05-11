# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/19
# Description: Keep Hungry Keep Foolish

import logging
from airtest.core.api import auto_setup, wake, connect_device
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 在实际项目中使用conftest.py中初始化的poco
# 由于直接在模块中无法使用pytest fixture，我们在第一次使用时初始化一次
poco = None

def initialize_poco_if_needed():
    """初始化poco（如果尚未初始化）"""
    global poco
    if poco is None:
        # 使用与conftest.py中相同的参数初始化
        poco = AndroidUiautomationPoco(use_airtest_input=True, 
                                      screenshot_each_action=False, 
                                      force_restart=False)  # 使用False避免重复初始化
    return poco

# 自动初始化
initialize_poco_if_needed()