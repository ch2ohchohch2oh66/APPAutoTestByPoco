#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from moduls.android.common.base_page import BasePage
from moduls.android.common.ui_elements import InMeetingElements
from moduls.android.common.poco_common import *
class InmeetingDefaultpage(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = InMeetingElements()

    def call_top_and_bottom_button(self):
        """显示顶部和底部按钮"""
        if not self.element_exists(self.elements.MORE_BUTTON):
            poco.click([0.5, 0.5])

    def click_more_button(self):
        """点击更多按钮"""
        if not self.element_exists(self.elements.MORE_BUTTON):
            poco.click([0.5, 0.5])
        self.wait_for_element(self.elements.MORE_BUTTON)
        self.click_element(self.elements.MORE_BUTTON)