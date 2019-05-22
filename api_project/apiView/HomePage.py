# -*- coding:utf-8 -*-
#
import requests


class HomePage:
    def home_page(self):
        uri = "http://172.16.0.210:3000/login/guider"
        resp = requests.get(url=uri)
        # print("首页：", resp.status_code)
        return resp.content.decode("utf-8")


if __name__ == '__main__':
    homep = HomePage()
    homep.home_page()
