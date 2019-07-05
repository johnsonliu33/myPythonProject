# -*- cocoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_prac():
    name_list = []
    utl = "https://www.runoob.com/python3/python3-examples.html"
    rep = requests.get(url=utl)
    html = rep.content.decode(encoding="utf-8")
    str1 = BeautifulSoup(html, "html.parser")
    str2 = str1.find(id="content")
    str3 = str2.find_all("a")
    for s in str3[1:]:
        href = s.get("href")
        href = "https://www.runoob.com" + href
        name = s.get_text()[7:].strip()
        name_list.append(name)
    return name_list


def save_file(name_list):
    for name in name_list:
        name = ".".join((name, "py"))
        with open(name, "w")as file:
            file.write("#")


if __name__ == '__main__':
    name_list = get_prac()
    save_file(name_list)
