# -*- coding:utf-8 -*-
import unittest
from BeautifulReport import BeautifulReport
import time


def start():
    test_dir = './src/testcase'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    result = BeautifulReport(suite)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="selenium自动化", log_path="./report")


if __name__ == '__main__':
    start()
