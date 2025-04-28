#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: 与UI无关的公共配置

import os.path

# 获取项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 等待时间常量
class WaitTime:
    """等待时间常量"""
    ULTRA_SHORT = 0.5  # 超短等待，用于极快速操作
    SHORT = 1         # 短等待，用于快速操作
    MEDIUM = 3        # 中等等待，用于一般操作
    LONG = 5          # 长等待，用于较慢操作
    EXTREME = 10      # 极长等待，用于极慢操作

# 应用包名配置
APP_PACKAGE = {
    'tencent_meeting': 'com.tencent.wemeet.app'
}

# 图片路径配置
IMAGE_PATHS = {
    'meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'homepage', 'meeting'),
    'book_meeting_image_path': os.path.join(PROJECT_ROOT, 'resources', 'android', 'book_meeting')
}

# 图片文件名配置
IMAGE_FILES = {
    'book_meeting': 'book_meeting.jpg',
    'next_step': 'next_step.jpg'
} 