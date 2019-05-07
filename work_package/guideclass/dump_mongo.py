# -*- coding:utf-8 -*- 

import time
import os

DBUSER = "guideclass"  # 用户
DBPASS = "zaq1xsw2"  # 密码
IP = "172.16.0.166"  # 主机
now = time.strftime("%Y-%m-%d")
DATA_DIR = "./back_data"  # 目录
DATA_BASE = "guideclass_ceshi"  # 库名
PATH_DUMP = "/usr/local/mongodb/bin/mongodump"  # 命令路径
BACKITEMS = ["%s -h %s:27017 -u %s -p %s -d %s -o %s" % (PATH_DUMP, IP, DBUSER, DBPASS, DATA_BASE, DATA_DIR), "pwd"]


def backData():
    try:
        for item in BACKITEMS:
            print("============" + item + "============")
            print(os.system(item))
    except RuntimeError:
        print("RuntimeError")


if __name__ == "__main__":
    backData()
