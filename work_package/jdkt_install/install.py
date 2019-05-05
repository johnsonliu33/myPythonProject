import requests
import re
import json

url = "http://download.jd100.com/ETClient/3.41.10.1902/"
url_json = "http://download.jd100.com/ETClient/3.41.10.1902/EasyClient.json"
res = requests.get(url)
json_str = requests.get(url_json)


def software():
    str_soft = ""
    keys = '<a href=".+?">(.+?)</a>'
    pattern = re.compile(keys)
    result = pattern.findall(res.text)
    c = 0
    for i in result:
        if i.endswith(".gz"):
            str_soft = str_soft + "," + i
            c += 1
        else:
            print("其他: " + i)
            pass
    print("soft count : ", c, "\n")
    return str_soft


params_json = json.loads(json_str.text)  # 将 JSON 对象转换为 Python 字典
items = params_json.items()
inst = software()
count = 0
for key, value in items:
    if key == "Modules" or key == "BetaModules":
        for j in value:
            k = j["name"]
            if k in inst:
                print(k + "\t\tok")
                count += 1
            else:
                print("\n" + j)
print("json count : ", count)
