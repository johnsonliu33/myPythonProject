# -*- coding:utf-8 -*-
import requests
import re
import json


def get_software(version):
    """获取当前版本应用程序"""
    heard = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Connection": "keep-alive",
        "Cookie": "sidebar_collapsed=false; _gitlab_session=0a41abf93ba979bf02ff6d11770f2f1e",
        "Host": "gitlab.easytech-main.com",
        "Referer": "http://gitlab.easytech-main.com/Package/AutomaticPublishETClient"
    }
    url = "http://gitlab.easytech-main.com/Package/AutomaticPublishETClient/tree/master/{}".format(version)
    resp = requests.get(url, headers=heard)
    string = resp.content.decode("utf-8")
    software_list = []
    keys = 'a title="(.+?)" href="/Package/AutomaticPublishETClient/blob/master/.+?">'
    pattern = re.compile(keys)
    result = pattern.findall(string)
    s_count = 0
    for i in result:
        if i.endswith(".gz"):
            software_list.append(i.split(".gz")[0])
            s_count += 1
        else:
            print("其他: {}".format(i))
            pass
    print("software count : {}\n".format(s_count))
    return software_list


def get_json(modules):
    """读取json文件"""
    with open("./EasyClient.json", "r", encoding="utf-8")as file:
        d = file.read()
    json_list = []
    params_json = json.loads(d)
    json_str = params_json.items()
    j_count = 0
    for key, value in json_str:
        if key == modules:
            for v in value:
                json_list.append(v["name"])
                try:
                    up = v["mustupdate"]
                    if up == "true":
                        print(v["name"], "==", up)
                except:
                    pass
                j_count += 1
    print("json count : {}\n".format(j_count))
    return json_list


def check_software(software_list, json_list):
    for item in json_list:
        if item in software_list:
            print("ok\t{}".format(item))
        else:
            print("[-] Not found ： {} ".format(item))
    print("====== end ======")


if __name__ == '__main__':
    version = "3.42.12.1905"
    modules = "Modules"
    beta_modules = "BetaModules"
    software_list = get_software(version)
    json_list = get_json(modules)
    check_software(software_list, json_list)
