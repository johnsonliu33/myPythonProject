# -*- coding:utf-8 -*-
import win32clipboard as clip
import win32com


class Clipboard:
    """实现剪贴板功能"""

    # 读取剪贴板内容
    @staticmethod
    def getText():
        # 打开剪贴板
        clip.OpenClipboard()
        # 获取剪贴板中的数据
        d = clip.GetClipboardData(win32com.CF_TEXT)
        # 关闭剪贴板
        clip.CloseClipboard()
        return d

    # 设置剪贴板内容
    @staticmethod
    def setText(aString):
        # 打开剪贴板
        clip.OpenClipboard()
        # 情况剪贴板
        clip.EmptyClipboard()
        # 将数据写入剪贴板
        # aString = str(aString).strip()
        clip.SetClipboardData(win32com.CF_UNICODETEXT, aString)
        # 关闭剪贴板
        clip.CloseClipboard()


if __name__ == '__main__':
    c = Clipboard
    c.setText("gfdsgfd")
    c.getText()
