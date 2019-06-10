# -*- coding:utf-8 -*-
import os
import requests
from lxml import html
from threading import Thread
import time

requests.packages.urllib3.disable_warnings()


def get_proxies(param):
    proxies = []
    url = "https://www.xicidaili.com/nn/{}".format(param)
    header_dict = {
        "User-Agent": """Mozilla/5.0 (Windows NT 6.1; WOW64)
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36""",
        'Connection': 'close',
    }
    try:
        resp = requests.get(url, verify=False, headers=header_dict, timeout=10)
        tree = html.fromstring(resp.text)
        class_odd_list = tree.xpath("//tr[@class='odd']")
        class_none_list = tree.xpath("//tr[@class='']")
        class_odd_list.extend(class_none_list)
        for elem_odd in class_odd_list:
            element_ip = elem_odd.xpath("./td[2]/text()")[0]
            element_port = elem_odd.xpath("./td[3]/text()")[0]
            proxy1 = element_ip + ":" + element_port
            proxies.append(proxy1)
        return proxies
    except Exception:
        print(url + " 请求失败！")


def save_proxies(proxy):
    with open("proxies.txt", "a")as file:
        file.write(proxy + "\n")


def read_proxies():
    if not os.path.exists("./proxies.txt"):
        print("[-]proxies.txt not exists!")
    else:
        with open("proxies.txt", "r")as file:
            proxies = file.readlines()
        return proxies


def check_proxy(proxy):
    url = "http://www.jd100.com/"
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Connection': 'close',
    }
    try:
        print(proxy)
        resp = requests.get(url=url, headers=header_dict, proxies={"http": proxy}, verify=False, timeout=10)
        if resp.status_code == 200:
            save_proxies(proxy)
            print(proxy)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)


def main(param):
    proxies_list = get_proxies(param)
    thread_list = []
    starttime = time.clock()
    if proxies_list is None:
        print("=====第", param, "页无代理IP=====")
        return None
    for proxy in proxies_list:
        thread_one = Thread(target=check_proxy, args=(proxy,))
        thread_list.append(thread_one)
    for temp in thread_list:
        temp.start()
    for temp in thread_list:
        temp.join()
    elapsed = (time.clock() - starttime)
    print("Time used: %.2f" % elapsed)


if __name__ == '__main__':
    # uri_param = ([x for x in range(1, 9)])
    # uri_param = [""] + uri_param
    # main_list = []
    # for param in uri_param:
    #     main_one = Thread(target=main, args=(param,))
    #     main_list.append(main_one)
    # for item in main_list:
    #     item.start()
    # for item in main_list:
    #     item.join()
    proxies = read_proxies()
    for proxy in proxies:
        check_proxy(proxy)
