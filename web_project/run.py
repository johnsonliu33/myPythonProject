# -*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import time
import os


def start():
    test_dir = './src/testcase'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    result = BeautifulReport(suite)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="selenium自动化", log_path="./report")


def reporty_path():
    report_dir = "./report"
    lists = os.listdir(report_dir)
    lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
    return lists[-1]


if __name__ == '__main__':
    start()
