# -*- coding:utf-8 -*-
#

import unittest


def start():
    test_dir = 'test_case'
    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print("一共测试 {} 条用例".format(suite.countTestCases()))


if __name__ == '__main__':
    start()
