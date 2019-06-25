# -*- coding: UTF-8 -*-
from pymongo import MongoClient


def collec_mongo1():
    # 建立和数据库系统的连接,指定host及port参数
    client1 = MongoClient('172.16.0.166', 27017)
    database1 = client1.guideclass_ceshi
    # 账号密码认证
    database1.authenticate("guideclass", "zaq1xsw2")
    # 查看全部表名称
    database1.collection_names()
    print(database1.collection_names())


def collec_mongo2():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client2 = MongoClient(uri)
    # A
    database2 = client2["guideclass_ceshi"]
    collection2 = database2.users
    user_list1 = collection2.find()
    for item1 in user_list1:
        print(item1)
    # B
    collection3 = client2["guideclass_ceshi"]["users"]
    user_list2 = collection3.find()
    for item2 in user_list2:
        print(item2)


class MongoUtil:
    def __init__(self, database="guideclass_ceshi", collect="test"):
        uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/%s" % database
        client = MongoClient(uri)
        self.collection = client[database][collect]

    def mongo_insert_one(self):
        # insert接收字典，返回object
        result = self.collection.insert_one({"username": "test01", "age": 33})
        print("insert_one: {}".format(result))

    def mongo_insert_many(self):
        item_list = [{"username": "test0{}".format(i)} for i in range(9)]
        # insert_many接收一个列表，列表中为所有要插入的字典
        results = self.collection.insert_many(item_list)
        # result2.insert_ids为所有插入的ID
        for item in results.inserted_ids:
            print("insert_many: {}".format(item))

    def mongo_find_one(self):
        # find_one查找并返回一个结果，接收一个字典形式的条件
        res_one = self.collection.find_one({"username": "test01"})
        print("find_one: {}".format(res_one))

    def mongo_find_many(self):
        # find返回所有满足条件的结果，如果条件为空，则返回数据库的所有
        res_list = self.collection.find({"username": "test01"})
        # 结果是一个Cursor游标对象，是一个可迭代对象，可以类似读文件的指针
        for i in res_list:
            print("find+: {}".format(i))
        for i in res_list:  # 此时res_list中没有内容
            print("find-: {}".format(i))

    def mongo_update_one(self):  # 只修改第一个符合条件的数据
        self.collection.update_one({"username": "test01"}, {
                                   "$set": {"username": "new_test01"}})

    def mongo_update_many(self):  # 修改所有符合条件的数据
        self.collection.update_many({"username": "test02"}, {
                                    "$set": {"username": "new_test02"}})

    def mongo_delete_one(self):  # 只删除第一个符合条件的数据
        self.collection.delete_one({"username": "test03"})

    def mongo_delete_many(self):  # 删除所有符合条件的数据
        self.collection.delete_many({"username": "test04"})

    def mongo_clear_collection(self):  # 删除所有数据
        self.collection.delete_many({})


# insert(),save(),update(),remove()已启用
if __name__ == '__main__':
    coll = MongoUtil()
    coll.mongo_insert_one()
    coll.mongo_insert_many()
    coll.mongo_find_one()
    coll.mongo_find_many()
    coll.mongo_update_one()
    coll.mongo_update_many()
    coll.mongo_delete_one()
    coll.mongo_delete_many()
    coll.mongo_clear_collection()
