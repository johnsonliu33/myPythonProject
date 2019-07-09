# -*- coding:utf-8 -*-
from pymongo import MongoClient
import pymysql


def mysqlUtil(sqlStr, username):
    host = "192.168.20.156"
    port = 3306
    user = "test_user"
    passwd = "test_user!@#123"
    db = "easyweb_new_trans"
    try:
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=passwd,
            database=db)
        cursor = conn.cursor()
        res = cursor.execute(sqlStr)
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def mongo_datebase():
    DATA_BASE = "guideclass_ceshi"
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/%s" % DATA_BASE
    client = MongoClient(uri)
    dataBase = client[DATA_BASE]
    return dataBase


def insert_user(username):
    sql_one = """INSERT INTO easyweb_new_trans.`W_UserBaseInfo`
                (`id`, `username`, `userpwd`, `realname`, `sex`, `email`, `schoolname`, `provincename`, `districtname`, `subdistrictname`, `grade`, `gradetype`, `classname`, `tel`, `mobile`, `isdelete`, `registertime`, `lastmodifytime`, `filepathid`, `registerip`, `usertype`, `knowtype`, `othertype`, `qqno`, `isipuser`, `easycash`, `userfigure`, `subjectclassify`, `subject`, `sourcetype`, `ipcode`, `ischargeaccount`, `isinvited`, `isdetailed`, `areacode`, `studyrecordemail`, `nickname`, `facedata`, `mobilebind`)
                VALUES
                (null, '%s', 'VMtLmys=', '', 2, '', '房山区青龙湖中学', '北京', '北京', '房山区', '02-2016', 0, '', '', '18888888888', 0, '2018-11-04 03:00:50', '2018-11-04 03:18:16', NULL, '111.199.221.70', 0, 0, '', '19790221', 0, 0, 4, 0, '', 0, '0000', 1, 1, 1, '', '', '', '', 1);""" % username
    mysqlUtil(sql_one, username)


def update_userPass(username):
    sql_two = "update W_UserBaseInfo set userpwd='VMtLmys=', realname='简而优'  where username ='%s';" % username
    mysqlUtil(sql_two, username)



def get_user():
    db = mongo_datebase()
    cellec_users = db.users
    data_users = cellec_users.find()
    num = 0
    for user in data_users:
        print("user: " + user["username"])
        # insert_user(user["username"])
        update_userPass(user["username"])
        num += 1
    print("有效用户：%s 个"% num)


def update_username():
    database=mongo_datebase()
    collect = database["users"]
    user_list = collect.find()
    for user in user_list:
        for key in user:
            if key == "realName":
                user_name_old = user["realName"]
                user_name_new = "内网-" + user_name_old
                collect.update_one({"realName": user_name_old}, {
                                   "$set": {"realName": user_name_new}})

def update_studentname():
    database=mongo_datebase()
    collect = database["students"]
    user_list = collect.find()
    for user in user_list:
        for key in user:
            if key == "realName":
                user_name_old = user["realName"]
                user_name_new = "内网-" + user_name_old
                collect.update_one({"realName": user_name_old}, {
                                   "$set": {"realName": user_name_new}})


if __name__ == '__main__':
    update_studentname()
