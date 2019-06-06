# -*- coding:utf-8 -*-

import requests
import re


def get_proxies():
    url = "https://www.xicidaili.com/nn/"
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    resp = requests.get(url, verify=True, headers=header_dict)
    print(resp.text)
    content = resp.text
    key1 = "<td>(\d+\.\d+\.\d+\.\d+)</td>"
    tempList1 = re.findall(key1, content)
    for temp in tempList1:
        print(temp)


if __name__ == '__main__':
    get_proxies()
