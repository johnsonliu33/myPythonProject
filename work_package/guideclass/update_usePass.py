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
        if res == 1:
            for i in cursor.fetchall():
                print(i)
        else:
            print(username + " 运行失败!!!")
    except Exception as e:
        print(e)
    finally:
        conn.commit()
        cursor.close()
        conn.close()


def mongo_datebase():
    DATA_BASE = "guideclass_ceshi2"
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/%s" % DATA_BASE
    client = MongoClient(uri)
    dataBase = client[DATA_BASE]
    return dataBase


def insert_user(username):
    sql_one = """INSERT INTO easyweb_new_trans.`W_UserBaseInfo`
                (`id`, `username`, `userpwd`, `realname`, `sex`, `email`, `schoolname`, `provincename`, `districtname`, `subdistrictname`, `grade`, `gradetype`, `classname`, `tel`, `mobile`, `isdelete`, `registertime`, `lastmodifytime`, `filepathid`, `registerip`, `usertype`, `knowtype`, `othertype`, `qqno`, `isipuser`, `easycash`, `userfigure`, `subjectclassify`, `subject`, `sourcetype`, `ipcode`, `ischargeaccount`, `isinvited`, `isdetailed`, `areacode`, `studyrecordemail`, `nickname`, `facedata`, `mobilebind`)
                VALUES
                (null, '{}', 'VMtLmys=', '', 2, '', '房山区青龙湖中学', '北京', '北京', '房山区', '02-2016', 0, '', '', '18888888888', 0, '2018-11-04 03:00:50', '2018-11-04 03:18:16', NULL, '111.199.221.70', 0, 0, '', '19790221', 0, 0, 4, 0, '', 0, '0000', 1, 1, 1, '', '', '', '', 1);""".format(
        username)
    mysqlUtil(sql_one, username)


def update_usePass(username):
    sql_two = "update W_UserBaseInfo set userpwd='VMtLmys=', realname='定制学生'  where username ='{}';".format(
        username)
    mysqlUtil(sql_two, username)


def get_user():
    db = mongo_datebase()
    cellec_users = db.users
    data_users = cellec_users.find()
    num = 0
    for user in data_users:
        print("user: " + user["username"])
        # insert_user(user["username"])
        # update_usePass(user["username"])
        num += 1


if __name__ == '__main__':
    get_user()
