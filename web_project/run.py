# -*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import time
import os
from web_project.src.util.send_email import send_email

dir_path = os.path.dirname(__file__)


def start():
    case_dir = os.path.join(dir_path, "src", "testcase")
    report_dir = os.path.join(dir_path, "src", "report")
    suite = unittest.defaultTestLoader.discover(case_dir, pattern='test_*.py')
    result = BeautifulReport(suite)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="selenium-测试报告", log_path=report_dir)


def reporty_path():
    report_dir = os.path.join(dir_path, "src", "report")
    lists = os.listdir(report_dir)
    lists.sort(key=lambda x: os.path.getatime(report_dir))  # 按文件时间排序
    latest_report = os.path.join(report_dir, lists[-1])
    send_email(latest_report)


if __name__ == '__main__':
    start()
    reporty_path()
