# -*- coding:utf-8 -*-
from time import sleep
from web_project.src.baseview.index_view import IndexView
from web_project.src.baseview.login_view import LoginView
from selenium import webdriver
from web_project.src.common.myunit import StartEnd


class TestZenTao(StartEnd):
    def test_login(self):
        username = "admin"
        password = "Mm123456"
        IndexView.test_zt_type(self.driver)
        LoginView.test_user_login(self.driver, username, password)
        title = self.driver.title
        assert title == u"我的地盘-禅道", "登录失败"
