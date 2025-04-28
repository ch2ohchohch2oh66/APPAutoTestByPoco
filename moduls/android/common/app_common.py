#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish

import logging
from time import sleep
from airtest.core.api import start_app, stop_app, wake
from configs.android.other_configs import APP_PACKAGE

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()  # 输出到控制台
    ]
)
# 显式设置 airtest 的日志级别为 INFO，如果需要的话，可以修改为 DEBUG 等级别
logging.getLogger('airtest').setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def open_android_app(package_name=APP_PACKAGE['tencent_meeting']):
    """
    Open the specified Android app_common.
    """
    stop_app(package_name)
    logger.info("关闭应用成功")
    sleep(1)
    start_app(package_name)
    logger.info("启动应用成功")

def close_android_app(package_name=APP_PACKAGE['tencent_meeting']):
    """
    Close the specified Android app_common.
    """
    logger.info("关闭应用")
    wake()
    stop_app(package_name)
    logger.info("关闭应用成功")


if __name__ == "__main__":
    # 使用配置文件中的应用包名
    open_android_app(APP_PACKAGE['tencent_meeting'])