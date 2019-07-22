# -*- coding:utf-8 -*-
import os


def input_data():
    DBUSER = "guideclass"
    DBPASS = "zaq1xsw2"
    IP = "172.16.0.166"  # 将数据导入改主机
    DATA_BASE = "guideclass_ceshi"
    DATA_DIR = "./data/guiderels.json"
    PATH_RES = "/usr/local/mongodb/bin/mongoimport"
    COLNAME = "guiderels"

    BACKITEMS = ["%s -h %s:27017 -u %s -p %s -d %s -c %s --file %s --type json" % (
        PATH_RES, IP, DBUSER, DBPASS, DATA_BASE, COLNAME, DATA_DIR)]
    try:
        for item in BACKITEMS:
            print("============" + item + "============")
            print(os.system(item))
    except RuntimeError:
        print(str("RuntimeError"))


if __name__ == "__main__":
    input_data()
