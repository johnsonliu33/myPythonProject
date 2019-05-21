# -*- coding:utf-8 -*-
#
import re
from api_project.apiView.action_login import LoginPage
from api_project.common.myUnittest import StartEnd


class test_login(StartEnd):
    def test_login_true(self):
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message": "(.+?)",'
        temp = re.findall(key, resp)
        print(temp)
        self.assertEqual(temp[0], "登录成功")

    def test_login_fasle(self):
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "22222"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message": "(.+?)",'
        temp = re.findall(key, resp)
        print(temp)
        self.assertEqual(temp[0], "用户名或密码错误")

    def test_login_fasle2(self):
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "22222"
        }
        loginp = LoginPage()
        resp = loginp.login_page(body)
        key = '"message": "(.+?)",'
        temp = re.findall(key, resp)
        print(temp)
        self.assertEqual(temp[0], "该账号未授权")
