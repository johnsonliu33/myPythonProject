# -*- coding:utf-8 -*- 
import os

DBUSER = "guideclass"  # 用户
DBPASS = "zaq1xsw2"  # 密码
IP = "172.16.0.166"  # 主机
DATA_DIR = "./data/guiderels.json"  # 目录
DATA_BASE = "guideclass_ceshi"
COLNAME = "guiderels"
PATH_DUMP = "/usr/local/mongodb/bin/mongoexport"  # 命令路径
BACKITEMS = ["%s -h %s:27017 -u %s -p %s -d %s -c %s -o %s --type json" % (
    PATH_DUMP, IP, DBUSER, DBPASS, DATA_BASE, COLNAME, DATA_DIR)]


def backData():
    try:
        for item in BACKITEMS:
            print("============" + item + "============")
            print(os.system(item))
    except RuntimeError:
        print(str("RuntimeError"))


if __name__ == "__main__":
    backData()
