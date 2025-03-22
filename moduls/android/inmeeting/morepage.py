#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: Keep Hungry Keep Foolish

from moduls.android.common.poco_common import *
from time import sleep

from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage


class Record(object):

    def start_record(self):
        logger.info('开启录制')
        poco(name='云录制', desc='云录制').click(sleep_interval=1)
        if poco(text='开启').exists():
            poco(text='开启').click(sleep_interval=1)
        logger.info('开启录制成功')

    def pause_record(self):
        logger.info('暂停录制')
        if poco(text='录制中').exists() and not poco(text='暂停').exists():
            poco(text='录制中').click(sleep_interval=1)
            poco(text='暂停').click(sleep_interval=1)
        logger.info('暂停录制成功')

    def restore_record(self):
        logger.info('恢复录制')
        if poco(text='录制暂停').exists():
            poco(text='录制暂停').click(sleep_interval=1)
            poco(text='恢复').click(sleep_interval=1)
        logger.info('恢复录制成功')

    def stop_record(self):
        logger.info('结束录制')
        if poco(text='录制中').exists():
            poco(text='录制中').click(sleep_interval=1)
            poco(text='结束').click(sleep_interval=1)
            poco(text='结束录制').click(sleep_interval=1)
        logger.info('结束录制成功')

    def record(self):
        InmeetingDefaultpage().call_top_and_bottom_button()
        sleep(0.5)
        InmeetingDefaultpage().click_more_button()
        sleep(1)
        self.start_record()
        sleep(5)
        self.pause_record()
        sleep(5)
        self.restore_record()
        sleep(5)
        self.stop_record()