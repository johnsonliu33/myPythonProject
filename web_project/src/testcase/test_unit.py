# -*- coding:utf-8 -*-
import sys
from selenium import webdriver
from time import sleep
import unittest


class TestUnit(unittest.TestCase):
    a = 6

    def sleep_three(self):
        sleep(3)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="../../driver/geckodriver.exe")
        cls.driver.implicitly_wait(8)

    def setUp(self):
        self.driver.get("http://www.baidu.com")
        print(self.driver.title)
        self.driver.maximize_window()

    def test_demo0(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "selenium_百度搜索", "title is fail")
        self.assertIn("selenium", self.driver.page_source, "title is fail")
        self.sleep_three()
        self.driver.refresh()
        self.sleep_three()
        self.driver.set_window_size(800, 800)
        self.sleep_three()
        self.driver.back()
        self.sleep_three()

    @unittest.skip("skipping")  # 无条件跳过
    def test_demo1(self):
        """百度搜索python"""
        self.driver.find_element_by_id("kw").send_keys("python")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "python_百度搜索", "title is fail")

    @unittest.skipIf(a > 5, "a>5=true")  # 如果a>5=true，则跳过
    def test_demo2(self):
        """百度搜索java"""
        self.driver.find_element_by_id("kw").send_keys("java")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "j              ava_百度搜索", "title is fail")

    @unittest.skipUnless(sys.platform.startswith("linux"), "request windows")  # 如果系统是Linux，则跳过
    def test_demo3(self):
        """百度搜索unittest"""
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "unittest_百度搜索", "title is fail")

    def tearDown(self):
        # self.driver.close()  # 关闭浏览器
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # 关闭geckodriver


if __name__ == '__main__':
    unittest.main()
