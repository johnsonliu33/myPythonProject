# -*- coding:utf-8 -*-
import win32com
import win32api


class KeyBoardKeys:
    """模拟键盘按键"""
    VK_CODE = {
        "enter": 0x0D,
        "ctrl": 0x11,
        "v": 0x56
    }

    @staticmethod
    def keyDown(keyname):
        # 按下按键
        win32api.keybd_event(KeyBoardKeys.VK_CODE[keyname], 0, 0, 0)

    @staticmethod
    def keyUp(keyname):
        # 释放按键
        win32api.keybd_event(KeyBoardKeys.VK_CODE[keyname], 0, win32com.KEYEVENTF_KEYUP, 0)

    @staticmethod
    def oneKey(key):
        # 模拟单个按键
        KeyBoardKeys.keyDown(key)
        KeyBoardKeys.keyUp(key)

    @staticmethod
    def towKeys(key1, key2):
        # 模拟单个按键
        KeyBoardKeys.keyDown(key1)
        KeyBoardKeys.keyDown(key2)
        KeyBoardKeys.keyUp(key1)
        KeyBoardKeys.keyUp(key2)
