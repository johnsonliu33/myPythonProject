# -*- coding:utf-8 -*-
#
import requests
import yaml


class LoginPage:
    def __init__(self):
        with open("../config/host.yaml", "r", encoding="utf-8") as file:
            self.host = yaml.full_load(file)
            print(self.host)

    def login_page(self, body):
        uri = "http://172.16.0.210:3000/api/login"
        session = requests.session()
        resp = session.post(url=uri, data=body)
        print("登录：", resp.status_code)
        return resp.content.decode("utf-8"), session


if __name__ == '__main__':
    loginp = LoginPage()
    body = {
        "role": "1",
        "username": "teacherlengjing",
        "password": "11111"
    }
    loginp.login_page(body)
