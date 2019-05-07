# -*- coding:utf-8 -*- 

import time

import os

DBUSER = "guideclass"

DBPASS = "zaq1xsw2"

IP = "172.16.0.166"  # 将数据导入改主机

DATA_BASE = "guideclass_ceshi"

DATA_DIR = "./back_data/guideclass_ceshi"

PATH_RES = "/usr/local/mongodb/bin/mongorestore"

BACKITEMS = ["%s -h %s:27017 -u %s -p %s -d %s --dir %s" % (PATH_RES, IP, DBUSER, DBPASS, DATA_BASE, DATA_DIR)]


def backData():
    try:

        for item in BACKITEMS:
            print("============" + item + "============")

            print(os.system(item))

    except RuntimeError:

        print(str("RuntimeError"))


if __name__ == "__main__":
    backData()
