# -*- coding:utf-8 -*-
import os
import requests
from lxml import html


def get_proxies():
    proxies = []
    url = "https://www.xicidaili.com/nn/"
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    resp = requests.get(url, verify=True, headers=header_dict)
    tree = html.fromstring(resp.text)
    class_odd_list = tree.xpath("//tr[@class='odd']")
    class_none_list = tree.xpath("//tr[@class='']")
    for elem_odd in class_odd_list:
        element_ip = elem_odd.xpath("./td[2]/text()")[0]
        element_port = elem_odd.xpath("./td[3]/text()")[0]
        proxy1 = element_ip + ":" + element_port
        proxies.append(proxy1)
    for elem_odd in class_none_list:
        element_ip = elem_odd.xpath("./td[2]/text()")[0]
        element_port = elem_odd.xpath("./td[3]/text()")[0]
        proxy2 = element_ip + ":" + element_port
        proxies.append(proxy2)
    return proxies


def save_proxies(proxy):
    if not os.path.exists("./proxies.txt"):
        with open("proxies.txt", "w")as file:
            file.write()
    with open("proxies.txt", "a")as file:
        file.write(proxy + "\n")


def read_proxies():
    if not os.path.exists("./proxies.txt"):
        print("proxies.txt not find!")
    with open("proxies.txt", "r")as file:
        proxies = file.readlines()
    return proxies


def check_proxy(proxy):
    url = "http://www.baidu.com/"
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        # 'Connection': 'close',
    }
    try:
        resp = requests.get(url=url, headers=header_dict, proxies={"http": proxy}, verify=False, timeout=1)
        if resp.status_code == 200:
            return True
        else:
            return False
    except Exception:
        pass


if __name__ == '__main__':
    proxies = get_proxies()
    for proxy in proxies:
        if check_proxy(proxy):
            save_proxies(proxy)
    proxies = read_proxies()
