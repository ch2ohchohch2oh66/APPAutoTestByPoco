#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from moduls.android.common.poco_common import *
class defaultpage_inmeeting(object):

    def call_top_and_bottom_button(self):
        if not poco(text='更多').exists():
            poco.click([0.5, 0.5])

    def click_more_button(self):
        if not poco(text='更多').exists():
            poco.click([0.5, 0.5])
        poco(text='更多').click()