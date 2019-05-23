# -*- coding:utf-8 -*-
#
import requests
import yaml
import os

class HomePage:
    def __init__(self):
        file_path = os.path.dirname(os.path.dirname(__file__))
        with open(file_path + "/config/host.yaml", "r", encoding="utf-8") as file:
            self.host = yaml.full_load(file)

    def home_page(self):
        uri = "http://" + self.host["host"] + ":3000" + "/login/guider"
        resp = requests.get(url=uri)
        # print("首页：", resp.status_code)
        return resp.content.decode("utf-8")


if __name__ == '__main__':
    homep = HomePage()
    homep.home_page()
