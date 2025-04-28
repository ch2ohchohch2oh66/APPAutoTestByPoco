#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: 测试基类，提供公共功能

import logging
from moduls.android.common.popup_handler import start_popup_handler, stop_popup_handler

logger = logging.getLogger(__name__)

class TestBase:
    """所有需要弹窗处理的测试类的基类"""
    
    @classmethod
    def setup_class(cls):
        """在测试类执行前调用一次，用于设置测试环境"""
        logger.info(f"==== 开始测试类 {cls.__name__} ====")
    
    @classmethod
    def teardown_class(cls):
        """在测试类执行后调用一次，用于清理测试环境"""
        logger.info(f"==== 测试类 {cls.__name__} 已完成 ====")

    @classmethod
    def setup_method(self, method):
        """在每个测试方法执行前调用"""
        logger.info(f"开始测试: {method.__name__}")

    @classmethod
    def teardown_method(self, method):
        """在每个测试方法执行后调用"""
        logger.info(f"测试完成: {method.__name__}") 