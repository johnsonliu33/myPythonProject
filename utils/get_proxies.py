# -*- coding:utf-8 -*-
import os

import requests
from lxml import html
from threading import Thread
import time
from random import randint

requests.packages.urllib3.disable_warnings()


def get_proxies(param):
    """
    获取代理ip
    :param param:
    :return:
    """
    proxies = []
    url = "https://www.xicidaili.com/nn/{}".format(param)
    header_dict = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Connection": "keep - alive",
        "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWMwNmJjNTg1NGQ5OWE5YmU0NDM5MTA5MTYwMTY3ZT"
                  "Y1BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXBNcG5FWFErOGpObHBqRFlkNlkwMVlFU0hrR3lpWkVubXZNeHpETFg1SmM9"
                  "BjsARg%3D%3D--5b3a942688ed8486d608d32440246cff4427f3d9; Hm_lvt_0cf76c77469e965d2957f0553e6ecf5"
                  "9=1561128103,1561128748,1561202507,1561297313; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1561298382",
        "If - None - Match": 'W / "7a5542968a39ef844ed66c00a251d96d"',
        "Accept - Language": "zh - CN, zh; q = 0.9"
    }
    try:
        time.sleep(randint(3, 10))
        resp = requests.get(url, verify=False, headers=header_dict, timeout=10)
        tree = html.fromstring(resp.text)
        class_odd_list = tree.xpath("//tr[@class='odd']")
        class_null_list = tree.xpath("//tr[@class='']")
        class_odd_list.extend(class_null_list)
        for elem_odd in class_odd_list:
            element_ip = elem_odd.xpath("./td[2]/text()")[0]
            element_port = elem_odd.xpath("./td[3]/text()")[0]
            proxy_type = elem_odd.xpath("./td[6]/text()")[0]
            proxy_ip = element_ip + ":" + element_port
            proxies.append(proxy_ip)
        return proxies
    except Exception as e:
        print(e)


def read_proxies():
    if not os.path.exists("./proxies.txt"):
        print("[-]proxies.txt not exists!")
    else:
        with open("proxies.txt", "r")as file:
            proxies = file.readlines()
        return proxies


def check_proxy(proxy):
    """
    校验代理ip是否可用
    :param proxy:
    :return:
    """
    url = "http://www.baidu.com/"
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Connection': 'close',
    }
    try:
        session = requests.session()
        session.keep_alive = False
        resp = session.get(
            url=url,
            headers=header_dict,
            proxies=proxy,
            verify=False,
            timeout=10)
        if resp.status_code == 200:
            return proxy
    except Exception:
        pass


def save_proxies(proxy):
    """
    保存可用的代理ip
    :param proxy:
    :return:
    """
    proxy_true = check_proxy(proxy)
    if proxy_true is not None:
        with open("proxies.txt", "a")as file:
            file.write(proxy_true + "\n")


def main(page):
    """多线程校验每页的IP是否可用,并保存到文件"""
    proxies_list = get_proxies(page)
    thread_list = []
    starttime = time.clock()
    if proxies_list is None:
        print("=====第", page, "页无代理IP=====")
        return None
    for proxy in proxies_list:
        thread_one = Thread(target=save_proxies, args=(proxy,))
        thread_list.append(thread_one)
    for temp in thread_list:
        temp.start()
    for temp in thread_list:
        temp.join()
    elapsed = (time.clock() - starttime)
    print("Time used: %.2f" % elapsed)


if __name__ == '__main__':
    """多线程抓取前9页代理IP"""
    uri_page = ([x for x in range(1, 9)])
    uri_page = [""] + uri_page
    main_list = []
    for page in uri_page:
        main_one = Thread(target=main, args=(page,))
        main_list.append(main_one)
    for item in main_list:
        item.start()
    for item in main_list:
        item.join()
    proxies = read_proxies()
    if proxies is not None:
        for proxy in proxies:
            check_proxy(proxy)
