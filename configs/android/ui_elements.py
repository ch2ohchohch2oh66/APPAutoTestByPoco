#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Andy Freeman
# Date: 2025/3/20
# Description: UI element locators configuration

class HomePageElements:
    # Bottom navigation
    MEETING_TAB = {'text': '会议'}
    CONTACTS_TAB = {'textMatches': '.*通讯录.*'}
    PROFILE_TAB = {'textMatches': '.*我的.*'}
    
    # Meeting page elements
    JOIN_MEETING = {'text': '加入会议'}
    QUICK_MEETING = {'text': '快速会议'}
    BOOK_MEETING = {'text': '预定会议'}
    SHARE_SCREEN = {'text': '共享屏幕'}
    
    # Meeting number input
    MEETING_NUMBER_INPUT = {'text': '请输入会议号'}
    JOIN_BUTTON = {'text': '加入会议', 'nameMatches': '.*xb$'}

class BookMeetingElements:
    # Book meeting elements
    MEETING_LIST = {'typeMatches': '.*RecyclerView'}
    MEETING_LIST_ITEMS = {'nameMatches': '.*ViewGroup$'}
    START_TIME = {'text': '开始时间'}
    CONFIRM_BUTTON = {'desc': '确定'}
    COMPLETE_BUTTON = {'text': '完成'}
    CONFLICT_PROMPT = {'text': '会议冲突提示'}
    BOOK_ANYWAY_BUTTON = {'text': '仍然预定'}
    CANCEL_BUTTON = {'text': '取消'}
    BACK_BUTTON = {'desc': '返回'}
    NEXT_STEP_BUTTON = {'text': '下一步'}
    
    # Time selection
    TIME_PICKER_START_POINT = [0.6, 0.8]
    TIME_PICKER_END_POINT = [0.6, 0.75]
    TIME_PICKER_DURATION = 0.5

class InMeetingElements:
    # Default page elements
    TURN_ON_VIDEO = {'text': '开启视频'}
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
    ALLOW = {'text': '允许'}
    DENY = {'text': '禁止'}
    POOR_NETWORK = {'text': '网络状况不佳'}
    CLOSE_VIDEO = {'text': '关闭视频'}
    NOTIFICATION = {'text': '开启消息通知'}
    THINK_AGAIN = {'text': '再想想'}
    NEXT_INSTALL = {'text': '下次安装'} 
    UPDATE_NOW = {'text': '立即更新'}
    CLOSE_UPDATE = {'nameMatches': '.*dj$'}
    
    # Advertisement popups
    SKIP_AD = {'text': '跳过'}  # 通用跳过按钮
    SKIP_AD_WITH_TIME = {'textMatches': '跳过[0-9]+s?'}  # 带倒计时的跳过按钮
    CLOSE_AD = {'desc': '关闭广告'}  # 关闭广告按钮
    CLOSE_AD_X = {'nameMatches': '.*关闭.*'}