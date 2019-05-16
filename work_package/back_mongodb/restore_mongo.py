# -*- coding:utf-8 -*- 
"""将数据导入该主机"""
from pymongo import MongoClient
import os

DBUSER = "guideclass"
DBPASS = "zaq1xsw2"
IP = "172.16.0.166"
DATA_BASE = "guideclass_ceshi2"
DATA_DIR = "./back_data/guideclass_ceshi2"
PATH_RES = "/usr/local/mongodb/bin/mongorestore"
BACKITEMS = ["%s -h %s:27017 -u %s -p %s -d %s --dir %s" % (PATH_RES, IP, DBUSER, DBPASS, DATA_BASE, DATA_DIR)]


def get_database():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi2"
    client = MongoClient(uri)
    database = client["guideclass_ceshi2"]
    return database


def clear_collection():
    database = get_database()
    for clear in database.collection_names():
        print("clear : ", clear)
        action = database[clear]
        action.delete_many({})


def back_data():
    clear_collection()
    try:
        for item in BACKITEMS:
            print("============" + item + "============")
            print(os.system(item))
    except RuntimeError as r:
        print("------" + r + "------")
    except Exception as e:
        print("------" + e + "------")


if __name__ == "__main__":
    back_data()
