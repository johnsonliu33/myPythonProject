# -*- coding:utf-8 -*-
import sys
from time import sleep
import unittest

from web_project.src.common.myunit import StartEnd
from web_project.src.common.common import save_img


class TestUnit(StartEnd):
    a = 1

    def sleep_three(self, num=1):
        sleep(num)

    @unittest.skip
    def test_demo0(self):
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
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
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("python")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "python_百度搜索", "title is fail")

    @unittest.skipIf(a > 5, "a>5=true")  # 如果a>5=true，则跳过
    def test_demo2(self):
        """百度搜索java"""
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("java")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        try:
            self.assertEqual(self.driver.title, "java-百度搜索", "title is fail")
        except BaseException:
            save_img(self.driver, "java_百度搜索.png")

    @unittest.skipUnless(sys.platform.startswith("Linux"),
                         "request windows")  # 如果系统不是Linux，则跳过
    def test_demo3(self):
        """百度搜索unittest"""
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.sleep_three()
        self.driver.find_element_by_id("su").click()
        self.sleep_three()
        self.assertEqual(self.driver.title, "unittest_百度搜索", "title is fail")
