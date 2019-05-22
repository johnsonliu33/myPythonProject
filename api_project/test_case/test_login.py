# -*- coding:utf-8 -*-
#
import re
from api_project.apiView.homePage import HomePage
import unittest
from api_project.apiView.actionLogin import LoginPage


class Test_Login(unittest.TestCase):
    def setUp(self):
        print("====== setUp ======")
        start = HomePage()
        cont = start.home_page()
        key = "<title>(.+?)</title>"
        temp = re.findall(key, cont)
        self.assertEqual(temp[0], "用户登录")

    def test_login_true(self):
        """登录-成功"""
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message":"(.+?)"'
        temp = re.findall(key, resp[0])
        self.assertEqual(temp[0], "登录成功")

    def test_login_fasle(self):
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "22222"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message":"(.+?)"'
        temp = re.findall(key, resp[0])
        self.assertEqual(temp[0], "用户名或密码错误")

    def test_login_fasle2(self):
        body = {
            "role": "1",
            "username": "https001",
            "password": "11111"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message":"(.+?)"'
        temp = re.findall(key, resp[0])
        self.assertEqual(temp[0], "该账号未授权")

    def tearDown(self):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main()
