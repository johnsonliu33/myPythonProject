import requests
import re
import json


def get_software(version):
    """获取当前版本应用程序"""
    url = "http://download.jd100.com/GuideStudent/{}/".format(version)
    res = requests.get(url)
    software_list = []
    keys = '<a href=".+?">(.+?)</a>'
    pattern = re.compile(keys)
    result = pattern.findall(res.text)
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


def get_json(version, modules):
    """获取当前版本json文件"""
    json_list = []
    url_json = "http://download.jd100.com/GuideStudent/{}/GCStudent.json".format(
        version)
    resp = requests.get(url_json)
    params_json = json.loads(resp.text)  # 将 JSON 对象转换为 Python 字典
    j_count = 0
    for key, value in params_json.items():
        if key == modules:
            for v in value:
                json_list.append(v["name"])
                try:
                    up = v["mustupdate"]
                    if up == "true":
                        print(v["name"], "==", up)
                except Exception:
                    pass
                j_count += 1
    print("json count : {}\n".format(j_count))
    return json_list


def check_software(software_list, json_list):
    for item in software_list:
        if item in json_list:
            print("ok\t{}".format(item))
        else:
            print("[-]  Not found software ： {} ".format(item))
    print("====== end ======")


if __name__ == '__main__':
    version = "1.0.3.1906"
    modules = "Modules"
    beta_modules = "BetaModules"
    software_list = get_software(version)
    json_list = get_json(version, modules)
    check_software(software_list, json_list)
