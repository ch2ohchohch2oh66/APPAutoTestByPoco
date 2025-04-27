#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/18
# Description: Keep Hungry Keep Foolish
from time import sleep

from moduls.android.inmeeting.record import Record
from moduls.android.inmeeting.defaultpage import InmeetingDefaultpage

def test_01_record():
    InmeetingDefaultpage().click_more_button()
    sleep(1)
    Record().start_record()
    sleep(3)
    Record().pause_record()
    sleep(3)
    Record().restore_record()
    sleep(3)
    Record().stop_record()
    sleep(1)

if __name__ == '__main__':
    test_01_record()

