# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest


class UnitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # cls.driver=webdriver.Chrome()
        # cls.driver=webdriver.Ie()
        cls.driver.implicitly_wait(8)

    def setUp(self):
        self.driver.get("http://www.baidu.com")
        print(self.driver.title)
        self.driver.maximize_window()

    def test_demo(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        title = self.driver.title()
        print(self.driver.title)
        self.assertEqual(title, "selenium_百度搜索", "title is fail")
        sleep(3)
        self.driver.refresh()
        self.driver.set_window_size(800, 800)
        sleep(3)
        self.driver.back()

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
