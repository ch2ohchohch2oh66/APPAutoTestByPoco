#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: UI element locators configuration

class HomePageElements:
    # Bottom navigation
    MEETING_TAB = {'nameMatches': '.*id/acn$', 'textMatches': '.*会议.*'}
    CONTACTS_TAB = {'nameMatches': '.*id/acn$', 'textMatches': '.*通讯录.*'}
    PROFILE_TAB = {'nameMatches': '.*id/acn$', 'textMatches': '.*我的.*'}
    
    # Meeting page elements
    JOIN_MEETING = {'text': '加入会议'}
    QUICK_MEETING = {'text': '快速会议'}
    BOOK_MEETING = {'text': '预定会议'}
    SHARE_SCREEN = {'text': '共享屏幕'}
    
    # Meeting number input
    MEETING_NUMBER_INPUT = {'text': '请输入会议号'}
    JOIN_BUTTON = {'text': '加入会议'}
    
    # Meeting controls
    END_MEETING = {'text': '结束'}
    TURN_ON_VIDEO = {'text': '开启视频'}

class InMeetingElements:
    # Default page elements
    MORE_BUTTON = {'text': '更多'}
    END_MEETING = {'text': '结束'}
    END_MEETING_CONFIRM = {'text': '结束会议'}
    END_MEETING_ACKNOWLEDGE = {'textMatches': '^我知道了.*$'}
    
    # Recording elements
    CLOUD_RECORDING = {'name': '云录制', 'desc': '云录制'}
    START_RECORDING = {'text': '开启'}
    PAUSE_RECORDING = {'text': '暂停'}
    RESUME_RECORDING = {'text': '恢复'}
    STOP_RECORDING = {'text': '结束'}
    RECORDING_STATUS = {'text': '录制中'}
    RECORDING_PAUSED = {'text': '录制暂停'}
    STOP_RECORDING_CONFIRM = {'text': '结束录制'}

class PopupElements:
    # Permission popups
    ALLOW_ONCE = {'text': '允许本次使用'}
    POOR_NETWORK = {'text': '网络状况不佳'}
    CLOSE_VIDEO = {'text': '关闭视频'}
    NOTIFICATION = {'text': '开启消息通知'}
    THINK_AGAIN = {'text': '再想想'}
    NEXT_INSTALL = {'text': '下次安装'}

class Timeouts:
    DEFAULT_WAIT = 5
    SHORT_WAIT = 3
    LONG_WAIT = 10
    POPUP_CHECK = 5
    POPUP_CLICK = 1
    POPUP_POLL = 0.5 