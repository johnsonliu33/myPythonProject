# -*- coding:utf-8 -*-
import datetime

from utils import excel_util
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
                    {"$and": [{"enrollYear": {"$lte": "2016"}},
                              {"gradeType": "gz3"}]},
                    {"$and": [{"enrollYear": {"$lte": "2015"}}, {"gradeType": "cz4"}]}]
    # query["gradeType"] = "cz3"
    projection = {}
    projection["username"] = "$username"
    projection["gradeType"] = "$gradeType"
    projection["enrollYear"] = "$enrollYear"
    projection["_id"] = 0

    cursor = c_students.find(query, projection=projection)
    return cursor


def get_guider(err_students):
    db = get_mongodb()
    c_guiderels = db.guiderels
    err_stu_list = []
    for err_student in err_students:
        query = {}
        query["student"] = err_student["username"]
        query["isValid"] = True
        query["endDate"] = {
            "$gt": datetime.datetime.utcnow()
        }

        projection = {}
        projection["guider"] = "$guider"
        projection["_id"] = 0

        sort = [("guider", -1)]

        cursor = c_guiderels.find(
            query, projection=projection, sort=sort, limit=1)
        if "dingzhi" not in err_student["username"] and "jianeryou" not in err_student[
                "username"]and "xued" not in err_student["username"]:
            for guider in cursor:
                es = err_student["username"], err_student["gradeType"], err_student["enrollYear"], guider["guider"]
                err_stu_list.append(es)
    return err_stu_list


def subject_type(var):
    return {
        "1": "语文",
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
        "6": "生物",
        "79": "史政",
        "8": "地理"
    }.get(var, "学科不存在！")


def get_exam():
    db = get_mongodb()
    c_guidereserves = db.guidereserves
    query = {}
    query["time"] = {
        "$lte": datetime.datetime.strptime("2019-07-22 08:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=FixedOffset(480, "+0800")),
        "$gte": datetime.datetime.strptime("2019-07-20 08:00:00.000000", "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=FixedOffset(480, "+0800"))
    }

    query["firstTime"] = False

    projection = {}
    projection["student"] = "$student"
    projection["subject"] = "$subject"
    projection["guider"] = "$guider"
    projection["time"] = "$time"
    projection["_id"] = 0

    cursor = c_guidereserves.find(query, projection=projection)

    stu_list = []
    for temp in cursor:
        if "dingzhi" not in temp["student"] and "jianeryou" not in temp["student"] and "https" not in temp["student"]:
            d = [
                temp["student"],
                subject_type(
                    temp["subject"]),
                temp["guider"],
                datetime.datetime.strftime(
                    temp["time"],
                    "%Y-%m-%d"),
                datetime.datetime.strftime(
                    temp["time"],
                    "%H:%M:%S")]
            stu_list.append(d)
    return stu_list


if __name__ == '__main__':
    # err_students = get_students()
    # err_stu_list = get_guider(err_students)
    # excel_util.write_excel("errorstudent.xlsx", err_stu_list)
    stu_list = get_exam()
    str_time = datetime.datetime.now().strftime("%Y-%m-%d")
    excel_util.write_excel(str_time+"_exam_student.xlsx", stu_list)
