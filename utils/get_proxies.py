# -*- coding:utf-8 -*-
import os
import requests
from lxml import html
from threading import Thread
import time
from random import randint

requests.packages.urllib3.disable_warnings()


def get_proxies(param):
    proxies = []
    url = "https://www.xicidaili.com/nn/{}".format(param)
    header_dict = {
        "User-Agent": """Mozilla/5.0 (Windows NT 6.1; WOW64)
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36""",
        "Connection": "keep - alive",
        "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWI1NDQ3Y2RiNzkwMjQ2OTkwNmIzYzdkOGJkODE4Y2RjBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMTFHSEJrNXRTTTZ1M0s2NWN5R0dmRjJad2tURWpRMlFZTVR6Y085c25qR289BjsARg%3D%3D--a5cf2f1542d86b22c3d23e4ba38c6322588d3010; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1561128103,1561128748; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1561128748",
        "If - None - Match": 'W / "7a5542968a39ef844ed66c00a251d96d"',
        "Accept - Language": "zh - CN, zh; q = 0.9"
    }
    try:
        time.sleep(randint(1, 5))
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


def read_proxies():
    if not os.path.exists("./proxies.txt"):
        print("[-]proxies.txt not exists!")
    else:
        with open("proxies.txt", "r")as file:
            proxies = file.readlines()
        return proxies


def check_proxy(proxy):
    url = "http://www.jd100.com/"
    proxy_list = []
    header_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'Connection': 'close',
    }
    try:
        resp = requests.get(url=url, headers=header_dict, proxies={"http": proxy}, verify=False,
                            timeout=10)
        if resp.status_code == 200:
            proxy_list.append(proxy)
        else:
            print(resp.status_code)
    except Exception as e:
        print(e)
    return proxy_list


def save_proxies(proxy):
    proxy_list = check_proxy(proxy)
    with open("proxies.txt", "a")as file:
        file.write(time.strftime("%Y-%m-%d") + ":\n")
        for p in proxy_list:
            file.write(p + "\n")


def main(param):
    proxies_list = get_proxies(param)
    thread_list = []
    starttime = time.clock()
    if proxies_list is None:
        print("=====第", param, "页无代理IP=====")
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
    uri_param = ([x for x in range(1, 9)])
    uri_param = [""] + uri_param
    main_list = []
    for param in uri_param:
        main_one = Thread(target=main, args=(param,))
        main_list.append(main_one)
    for item in main_list:
        item.start()
    for item in main_list:
        item.join()
    proxies = read_proxies()
    for proxy in proxies:
        check_proxy(proxy)
