#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Base page object class

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from moduls.android.common.poco_common import *
from moduls.android.common.ui_elements import Timeouts

class BasePage:
    def __init__(self):
        self.poco = poco
        self.timeout = Timeouts.DEFAULT_WAIT

    def wait_for_element(self, element_locator, timeout=None):
        """Wait for an element to appear on the screen"""
        timeout = timeout or self.timeout
        try:
            self.poco(**element_locator).wait_for_appearance(timeout)
            return True
        except PocoNoSuchNodeException:
            return False

    def click_element(self, element_locator, sleep_interval=1):
        """Click on an element if it exists"""
        if self.wait_for_element(element_locator):
            self.poco(**element_locator).click(sleep_interval=sleep_interval)
            return True
        return False

    def element_exists(self, element_locator):
        """Check if an element exists"""
        return self.poco(**element_locator).exists()

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