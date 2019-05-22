# -*- coding:utf-8 -*-
#
import requests
import re

class LoginPage:
    def login_page(self, body):
        uri = "http://172.16.0.210:3030/api/login"
        session=requests.session()
        resp = session.post(url=uri, data=body)
        print("登录：", resp.status_code)
        return resp.content.decode("utf-8"),session


if __name__ == '__main__':
    loginp = LoginPage()
    body = {
        "role": "1",
        "username": "teacherlengjing",
        "password": "11111"
    }
    loginp.login_page(body)
