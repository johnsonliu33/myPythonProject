# -*- coding:utf-8 -*-
import datetime
import pymysql
from utils import excel_util
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
    projection = {}
    projection["username"] = "$username"
    projection["gradeType"] = "$gradeType"
    projection["enrollYear"] = "$enrollYear"
    projection["_id"] = 0

    cursor = c_students.find(query, projection=projection)
    return cursor


def get_guider(err_students):
    """获取年级错误的学生信息"""
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
            "username"] and "xued" not in err_student["username"]:
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


def grade_type(var):
    return {
        "cz": "初中",
        "gz": "高中"
    }.get(var, "年级不存在！")


def get_student_isValide(student, subject):
    """判断学生的学科是否有效"""
    end_time = datetime.datetime(2019, 8, 3, 0, 0, 0)
    end_time = end_time + datetime.timedelta(hours=-8)
    db = get_mongodb()
    c_guiderels = db.guiderels.find({"student": student, "subject": subject})
    for temp in c_guiderels:
        if temp["isValid"] is True and temp["endDate"] >= end_time:
            return True
        else:
            return False


def get_grade_info(stu):
    """获取年级信息"""
    db = get_mongodb()
    c_guiderels = db.guiderels.find({"student": stu}).limit(1)
    for temp in c_guiderels:
        return temp["gradeType"]


def get_exam():
    """要测试的学生"""
    db = get_mongodb()
    c_guidereserves = db.guidereserves
    bigin_time = datetime.datetime(2019, 8, 3, 0, 0, 0)
    bigin_time = bigin_time + datetime.timedelta(hours=-8)
    end_time = datetime.datetime(2019, 8, 5, 0, 0, 0)
    end_time = end_time + datetime.timedelta(hours=-8)
    query = {}
    query["time"] = {
        "$lte": end_time,
        "$gte": bigin_time
    }
    query["isValid"] = True
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
            if get_student_isValide(temp["student"], temp["subject"]):
                text = [temp["student"], subject_type(temp["subject"]),
                        temp["guider"],
                        grade_type(get_grade_info(temp["student"])),
                        (temp["time"] + datetime.timedelta(hours=+8)).strftime("%Y-%m-%d"),
                        (temp["time"] + datetime.timedelta(hours=+8)).strftime("%H:%M")]
                stu_list.append(text)
    return stu_list


def get_answerinfo(guids):
    """查询同类题答案"""
    conn = pymysql.connect(
        host="192.168.1.179",
        port=3306,
        user="etwebRead",
        passwd="etwebRead123",
        db="easyweb")
    cursor = conn.cursor()
    sql_one = "SELECT * FROM W_SameSectionInfo WHERE guid = '%s'" % guids
    res = cursor.execute(sql_one)
    if res > 0:
        res_lesson = cursor.fetchall()
        return res_lesson[0][8]
    else:
        return "--"
    cursor.close()
    conn.close()


def check_sameSection():
    """查询做题结果"""
    db = get_mongodb()
    data_studysteps = db.studysteps
    document = data_studysteps.find({})
    for temp in document:
        if "ss:" in temp["sectionId"] and "content" in temp and "|" in temp["content"]:
            guids = temp["sectionId"].split(":")
            answer_num = len(temp["content"].split("|"))
            guids = guids[1]
            answer = get_answerinfo(guids)
            answer_two = len(answer.split("}"))
            if answer_num > answer_two:
                print(temp["student"], "==", temp["subject"], "==", temp["sectionId"], "==", answer_num, "==",
                      answer_two)


if __name__ == '__main__':
    # err_students = get_students()
    # err_stu_list = get_guider(err_students)
    # excel_util.write_excel("errorstudent.xlsx", err_stu_list)

    stu_list = get_exam()
    str_time = datetime.datetime.now().strftime("%Y-%m-%d")
    excel_util.write_excel(str_time + "_月测学生.xlsx", stu_list)

    # check_sameSection()
