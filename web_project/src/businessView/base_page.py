# -*- coding:utf-8 -*-
from time import sleep


class BasePage:
    """页面基础类"""

    def __init__(self, driver):
        self.base_url = "http://localhost"
        self.driver = driver
        self.timeout = 8

    def _open(self, api):
        _url = self.base_url + api
        print("Test page is : %s" % _url)
        self.driver.maximize_window()
        self.driver.get(_url)
        sleep(2)
        assert self.driver.current_url == _url, "Did ont land on %s" % _url

    def open(self, api):
        self._open(api)

    def get_element(self, *loc):
        return self.driver.find_element(*loc)
