# -*- coding:utf-8 -*-
import datetime

import xlwt
from bson.tz_util import FixedOffset
from pymongo import MongoClient


def get_mongodb():
    uri = "mongodb://dev:dev123@172.16.0.167:27017/guideclass"
    client = MongoClient(uri)
    db = client["guideclass"]
    return db


def get_students():
    db = get_mongodb()
    c_students = db.students

    query = {}
    query["$or"] = [{"$and": [{"enrollYear": {"$lte": "2016"}}, {"gradeType": "cz3"}]},
                    {"$and": [{"enrollYear": {"$lte": "2016"}}, {"gradeType": "gz3"}]}]
    query["gradeType"] = "cz3"
    projection = {}
    projection["username"] = "$username"
    projection["_id"] = 0

    err_students = c_students.find(query, projection=projection)
    return err_students


def get_guider(err_student):
    db = get_mongodb()
    c_guiderels = db.guiderels
    result=[]

    query = {}
    query["student"] = err_student["username"]
    query["isValid"] = True
    query["endDate"] = {
        "$gt": datetime.datetime.strptime("2019-04-21 08:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(480, "+0800"))
    }

    projection = {}
    projection["guider"] = "$guider"
    projection["_id"] = 0

    sort = [ ("guider", 1) ]

    guider = c_guiderels.find(query, projection = projection, sort = sort,limit = 1)
    for g in guider:
        g_data=err_student["username"]+":"+g["guider"]
        with open("error_grade_student.txt","a")as file :
            file.write(g_data+"\n")
    return result

def subject_type(var):
    return {
        "1":"语文",
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
        "6":"生物",
        "79":"史政",
        "8":"地理"
    }.get(var, "学科不存在！")

def get_exam():
    db = get_mongodb()
    c_guidereserves = db.guidereserves
    query = {}
    query["time"] = {
        u"$lte": datetime.datetime.strptime("2019-07-22 08:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(480, "+0800")),
        u"$gte": datetime.datetime.strptime("2019-07-20 08:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo = FixedOffset(480, "+0800"))
    }

    query["firstTime"] = False
    query["isValid"] = True

    projection = {}
    projection["student"] = "$student"
    projection["subject"] = "$subject"
    projection["guider"] = "$guider"
    projection["time"] = "$time"
    projection["_id"] = 0.0

    cursor = c_guidereserves.find(query, projection = projection, skip = 1007, limit = 1000)
    excel = xlwt.Workbook(encoding = 'utf-8')  # 创建一个Excel
    sheet = excel.add_sheet('Sheet1')  # 在其中创建一个名为hello的sheet
    stu_list=[]
    for temp in cursor:
        if "dingzhi" not in temp["student"] and "jianeryou" not in temp["student"]:
            d=[temp["student"],subject_type(temp["subject"]),temp["guider"],datetime.datetime.strftime(temp["time"], "%Y-%m-%d %H:%M:%S")]
            stu_list.append(d)
    for i in range(len(stu_list)):
        for j in  range(4):
            sheet.write(i, j, stu_list[i][j])  # 往sheet里第一行第一列写一个数据
    excel.save("exam_student.xlsx")


if __name__ == '__main__':
    # err_students=get_students()
    # for stu in err_students:
    #     get_guider(stu)
    get_exam()