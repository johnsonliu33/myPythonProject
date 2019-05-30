# -*- coding:utf-8 -*-

import os

report_dir = "./report"

lists = os.listdir(report_dir)
print(lists[-1])
lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
print(os.path.getatime(report_dir))
print("==" + lists[-1])
