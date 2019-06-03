# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest


class UnitDemo(unittest.TestCase):

    def sleep_three(self):
        sleep(3)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(8)

    def setUp(self):
        self.driver.get("http://www.baidu.com")
        print(self.driver.title)
        self.driver.maximize_window()

    def test_demo(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "selenium_百度搜索", "title is fail")
        self.sleep_three()
        self.driver.refresh()
        self.sleep_three()
        self.driver.set_window_size(800, 800)
        self.sleep_three()
        self.driver.back()
        self.sleep_three()

    def tearDown(self):
        self.driver.close()  # 关闭浏览器

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 关闭geckodriver


if __name__ == '__main__':
    unittest.main()
