# -*- coding:utf-8 -*-
#

import unittest

import time
from BeautifulReport import BeautifulReport


def start():
    test_dir = 'test_case'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    result = BeautifulReport(suite)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="双师精品课-学管师", log_path="./report")


if __name__ == '__main__':
    start()
