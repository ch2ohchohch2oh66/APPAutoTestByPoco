#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/4/27
# Description: Keep Hungry Keep Foolish

import logging
import pytest
import os
import sys
# 导入弹窗处理模块
from moduls.android.common.popup_handler import start_popup_handler, stop_popup_handler

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # 输出到控制台
    ]
)
logger = logging.getLogger(__name__)

# 将项目根目录添加到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)



# 会话级别的fixture，用于处理弹窗
@pytest.fixture(scope="session", autouse=True)
def handle_popup_fixture():
    """自动启动和停止弹窗处理的会话级别fixture"""
    # 启动弹窗处理
    start_popup_handler()
    
    # 等待测试执行
    yield
    
    # 停止弹窗处理
    stop_popup_handler()