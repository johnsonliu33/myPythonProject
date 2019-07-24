# -*- coding:utf-8 -*-
"""将数据导入该主机"""
import sys
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import os


def get_database(DATA_BASE):
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/{}".format(
        DATA_BASE)
    try:
        client = MongoClient(uri)
        database = client[DATA_BASE]
    except ServerSelectionTimeoutError as sste:
        print(sste)
        exit("database error!!!")
    return database


def clear_collection(database):
    """清空所有collection，刪除meetingtime"""
    for temp in database.collection_names():
        print("clear : ", temp)
        collect = database[temp]
        # 清除collection
        collect.delete_many({})
        if collect == "meetingtimes":
            # 刪除meetingtime
            collect.drop()


def back_data(BACKITEMS):
    try:
        for item in BACKITEMS:
            # print("============" + item + "============")
            print(os.system(item))
    except RuntimeError as r:
        print("------" + r + "------")
    except Exception as e:
        print("------" + e + "------")


def update_username(database):
    collect = database["users"]
    user_list = collect.find()
    for user in user_list:
        # if "realName" in user:
        if "realName" in user.keys():
            user_name_old = user["realName"]
            user_name_new = "内网-" + user_name_old
            collect.update_one({"realName": user_name_old}, {
                               "$set": {"realName": user_name_new}})


def update_studentname(database):
    collect = database["students"]
    user_list = collect.find()
    for user in user_list:
        if "realName" in user.keys():
            user_name_old = user["realName"]
            user_name_new = "内网-" + user_name_old
            collect.update_one({"realName": user_name_old}, {
                               "$set": {"realName": user_name_new}})


def restore(back_path, db_name):
    IP = "172.16.0.166"
    DBUSER = "guideclass"
    DBPASS = "zaq1xsw2"
    DATA_BASE = "guideclass_" + db_name
    DATA_PATH = "./back_data/{}".format("guideclass_" + back_path)
    PATH_RES = "/usr/local/mongodb/bin/mongorestore"
    BACKITEMS = ['%s -h %s:27017 -u %s -p %s -d %s --dir %s' % (PATH_RES, IP, DBUSER, DBPASS, DATA_BASE, DATA_PATH),
                 'date +"%Y-%m-%d %T"']
    database = get_database(DATA_BASE)
    clear_collection(database)
    back_data(BACKITEMS)
    update_username(database)
    update_studentname(database)


def main():
    usage = """[-]usage: restore_mongo.py <FILE_NAME> <DB_NAME>
            eg : python restore_mongo.py guideclass_0721 guideclass_ceshi2"""
    if len(sys.argv) < 3:
        print(usage)
    else:
        restore(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
