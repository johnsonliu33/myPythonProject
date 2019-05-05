'''
首测时间、每次定制面谈时间、面谈次数和爽约次数,购课时间

首测时间：studentdatas -- firstExamTime
面谈时间：studytasks  -- updatedAt
面谈次数：studentdatas -- guideTimes
爽约次数：studentdatas -- absentTimes
购课时间：guiderels -- orderDate
学生姓名：users -- realName

'''

from xlrd import open_workbook
from xlutils.copy import copy
import datetime
from pymongo import MongoClient


def subject_type(var):
    return {
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
    }.get(var, "-")


def write_data(data):
    rexcel = open_workbook("guideInfo.xls")  #
    rows = rexcel.sheets()[0].nrows
    excel = copy(rexcel)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0)
    for i in range(len(data)):
        print(data)
        table.write(rows, i, data[i])
    excel.save("guideInfo.xls")


def select_mongodb():
    # uri="mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    uri = "mongodb://dev:dev123@172.16.0.167:27017/guideclass"
    client = MongoClient(uri)
    # guideclass_db = client["guideclass_ceshi"]
    guideclass_db = client["guideclass"]
    return guideclass_db


# 查询首测时间、面谈次数、爽约次数
def select_student_for_studentdatas(students, subjects):
    db = select_mongodb()
    studentdatas_table = db.studentdatas
    studentdatas_data = studentdatas_table.find({"student": students, "subject": subjects})
    res1 = ""
    res2 = ""
    res3 = ""
    for stu_dt in studentdatas_data:
        if "guideTimes" in stu_dt.keys():
            res1 = stu_dt["guideTimes"]
        else:
            res1 = "-"
        if "absentTimes" in stu_dt.keys():
            res2 = stu_dt["absentTimes"]
        else:
            res2 = "-"
        if "firstExamTime" in stu_dt.keys():
            res3 = (stu_dt["firstExamTime"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            res3 = "-"
    res = (res1, res2, res3)
    return res


# 查询面谈时间
def select_student_for_studytasks(students, subjects, orderdates):
    db = select_mongodb()
    studytasks_table = db.studytasks
    studytasks_data = studytasks_table.find({"student": students, "subject": subjects})
    miantan = select_student_for_studentdatas(students, subjects)
    for stu_tk in studytasks_data:
        if stu_tk["updatedAt"] is not None:
            res_two = (stu_tk["updatedAt"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            res_two = "-"
        result_date1 = (students, subject_type(subjects), orderdates, res_two)
        result_date_all = result_date1 + miantan
        write_data(result_date_all)


def select_student_for_guider():
    db = select_mongodb()
    guiderels_table = db.guiderels
    guiderels_data = guiderels_table.find({"isValid": True})
    for guide_rel in guiderels_data:
        students = guide_rel["student"]
        subjects = guide_rel["subject"]
        orderdates = (guide_rel["orderDate"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        select_student_for_studytasks(students, subjects, orderdates)


if __name__ == "__main__":
    select_student_for_guider()
