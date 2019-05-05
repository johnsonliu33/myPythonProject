#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from pymongo import MongoClient

#建立和数据库系统的连接,指定host及port参数
client = MongoClient('172.16.0.166', 27017)
#连接mydb数据库-账号密码认证
db = client.guideclass_ceshi
db.authenticate("guideclass", "zaq1xsw2")
#连接表
collection = db.guiderworktimes
 
 
#查看全部表名称
db.collection_names()
print (db.collection_names())
  
#访问表的数据,过滤查询
item = collection.find({"guider":"https003"})
for rows in item:
    print (rows.values())
 
#访问表的一行数据
print (collection.find_one())


