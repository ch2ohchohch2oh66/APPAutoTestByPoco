#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Base page object class

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from moduls.android.common.poco_common import *
from configs.android.other_configs import WaitTime, MAX_RETRY

class BasePage:
    def __init__(self):
        self.poco = poco
        self.timeout = WaitTime.LONG
        self.sleep_interval = WaitTime.SHORT

    def wait_for_element(self, element_locator, timeout=None):
        """Wait for an element to appear on the screen"""
        timeout = timeout or self.timeout
        try:
            self.poco(**element_locator).wait_for_appearance(timeout)
            logger.info(f"Element {element_locator} appeared.")
            return True
        except PocoNoSuchNodeException:
            return False

    def click_element(self, element_locator):
        """Click on an element if it exists"""
        if self.wait_for_element(element_locator):
            self.poco(**element_locator).click(sleep_interval=self.sleep_interval)
            return True
        return False

    def click_existed_element(self, element_locator):
        if self.element_exists(element_locator):
            logger.info(f"Element {element_locator} exists, clicking it.")
            self.poco(**element_locator).click(sleep_interval=self.sleep_interval)
        else:
            logger.info(f"Element {element_locator} does not exist, skipping click.")

    def element_exists(self, element_locator):
        """Check if an element exists"""
        return self.poco(**element_locator).exists()
    
    def wait_element_exists(self, element, max_retries=MAX_RETRY, interval=WaitTime.MEDIUM):
        """
        检查元素是否存在，失败时自动重试
        :param element: 元素定位
        :param retries: 最大重试次数
        :param interval: 每次重试间隔秒数
        :return: True/False
        """
        for attempt in range(max_retries):
            if self.element_exists(element):
                return True
            if attempt < max_retries - 1:
                logger.warning(f'元素未找到，{interval}s后重试({attempt+1}/{max_retries})...')
                sleep(interval)
        logger.error(f'重试{max_retries}次后元素依然未找到')
        return False

    def get_element_text(self, element_locator):
        """Get text of an element if it exists"""
        if self.wait_for_element(element_locator):
            return self.poco(**element_locator).get_text()
        return None

    def set_element_text(self, element_locator, text):
        """Set text of an element if it exists"""
        if self.wait_for_element(element_locator):
            self.poco(**element_locator).set_text(text)
            return True
        return False

    def swipe_element(self, element_locator, direction='up', duration=0.5):
        """Swipe an element in a given direction"""
        if self.wait_for_element(element_locator):
            element = self.poco(**element_locator)
            if direction == 'up':
                element.swipe('up', duration=duration)
            elif direction == 'down':
                element.swipe('down', duration=duration)
            elif direction == 'left':
                element.swipe('left', duration=duration)
            elif direction == 'right':
                element.swipe('right', duration=duration)
            return True
        return False 