# -*- coding:utf-8 -*-
#
import requests


class HomePage:
    def home_page(self):
        headers = {
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
            "Accept-Encoding: gzip, deflate, br",
            "Accept-Language: zh-CN,zh;q=0.9",
            "Proxy-Connection: keep-alive",
            "Accept-Encoding: gzip, deflate",
            "Upgrade-Insecure-Requests: 1"}
        uri = "http://172.16.0.210:3000/login/guider"
        resp = requests.get(url=uri)
        print("首页：",resp.status_code)
        return resp.content.decode("utf-8")


if __name__ == '__main__':
    homep = HomePage()
    homep.home_page()
