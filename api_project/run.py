# -*- coding:utf-8 -*-
#

import unittest


def start():
    test_dir = 'test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(discover)


if __name__ == '__main__':
    start()
