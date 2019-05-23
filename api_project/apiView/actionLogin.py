# -*- coding:utf-8 -*-
#
import requests
import yaml
import os


class LoginPage:
    def __init__(self):
        file_path = os.path.dirname(os.path.dirname(__file__))
        with open(file_path + "/config/host.yaml", "r", encoding="utf-8") as file:
            self.host = yaml.full_load(file)

    def login_page(self, body):
        uri = "http://" + self.host["host"] + ":3030" + "/api/login"
        session = requests.session()
        resp = session.post(url=uri, data=body)
        # print("登录：", resp.status_code)
        return resp.content.decode("utf-8"), session


if __name__ == '__main__':
    loginp = LoginPage()
    body = {
        "role": "1",
        "username": "teacherlengjing",
        "password": "11111"
    }
    loginp.login_page(body)
