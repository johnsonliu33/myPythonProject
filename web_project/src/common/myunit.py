# -*- coding:utf-8 -*-
import unittest

import os
from selenium import webdriver


class StartEnd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driver_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        driver_file = os.path.join(driver_dir, "driver", "geckodriver.exe")
        cls.driver = webdriver.Firefox(executable_path=driver_file)
        cls.driver.implicitly_wait(10)

    def setUp(self):
        print(self.driver.title)

    def tearDown(self):
        # self.driver.close()  # 关闭浏览器
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 关闭geckodriver


if __name__ == '__main__':
    unittest.main()
