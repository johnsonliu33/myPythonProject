# -*- coding: UTF-8 -*-
from pymongo import MongoClient


def collec_mongo1():
    # 建立和数据库系统的连接,指定host及port参数
    client = MongoClient('172.16.0.166', 27017)
    database = client.guideclass_ceshi
    # 账号密码认证
    database.authenticate("guideclass", "zaq1xsw2")
    # 查看全部表名称
    database.collection_names()
    print(database.collection_names())

    # 连接表
    collection = database.users
    # 访问表的数据,过滤查询
    user_list = collection.find({"username": "https003"})
    for item in user_list:
        print(item.values())
    # 访问表的一行数据
    print(collection.find_one())


def collec_mongo2():
    ##链接MongoDB
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client = MongoClient(uri)
    database = client["guideclass_ceshi"]
    collection = database.users
