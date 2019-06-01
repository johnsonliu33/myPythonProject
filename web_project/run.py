# -*- coding:utf-8 -*-
import unittest
from HTMLTestRunner import BSTestRunner
import time
import os


def start():
    test_dir = './src/testcase'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report.html"
    fp= open(report_name,"wb")
    runner=BSTestRunner.BSTestRunner(stream=fp,title="Test report", description="selenium自动化")
    runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'
    runner.run(suite)


def reporty_path():
    report_dir = "./report"
    lists = os.listdir(report_dir)
    lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
    return lists[-1]


if __name__ == '__main__':
    start()
