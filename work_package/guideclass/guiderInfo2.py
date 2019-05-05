'''
首测时间、每次定制面谈时间、面谈次数和爽约次数,购课时间

首测时间：studentdatas -- firstExamTime
面谈时间：studytasks  -- updatedAt
面谈次数：studentdatas -- guideTimes
爽约次数：studentdatas -- absentTimes
购课时间：guiderels -- orderDate
学生姓名：users -- realName

'''
import datetime
from pymongo import MongoClient


def select_mongodb():
    # uri="mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    uri = "mongodb://dev:dev123@172.16.0.167:27017/guideclass"
    client = MongoClient(uri)
    # guideclass_db = client["guideclass_ceshi"]
    guideclass_db = client["guideclass"]
    return guideclass_db


# 查询面谈时间
def select_student_for_studytasks(student, subject):
    db = select_mongodb()
    studytasks_table = db.studytasks
    studytasks_data = studytasks_table.find({"student": student, "subject": subject})
    myFile.write("\n面谈时间：")
    for stu_tk in studytasks_data:
        if stu_tk["updatedAt"] is not None:
            res_two = (stu_tk["updatedAt"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            res_two = "-"
        myFile.write("\n\t " + res_two)


# 查询首测时间、面谈次数、爽约次数
def select_student_for_studentdatas(student, subject):
    db = select_mongodb()
    studentdatas_table = db.studentdatas
    studentdatas_data = studentdatas_table.find({"student": student, "subject": subject})
    for stu_dt in studentdatas_data:
        if "guideTimes" in stu_dt.keys():
            res1 = stu_dt["guideTimes"]
        else:
            res1 = "-"
        myFile.write("\n面谈次数：\t" + str(res1))
        if "absentTimes" in stu_dt.keys():
            res2 = stu_dt["absentTimes"]
        else:
            res2 = "-"
        myFile.write("\n迟到次数：\t" + str(res2))
        if "firstExamTime" in stu_dt.keys():
            res3 = (stu_dt["firstExamTime"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        else:
            res3 = "-"
        myFile.write("\n首测时间：\t" + res3)


def subject_type(var):
    return {
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
    }.get(var, "-")


def select_student_for_guider():
    db = select_mongodb()
    guiderels_table = db.guiderels
    guiderels_data = guiderels_table.find({"isValid": True})
    for guide_rel in guiderels_data:
        myFile.write("\n\n\n学生账号：\t" + guide_rel["student"])
        myFile.write("\n科目：\t" + subject_type(guide_rel["subject"]))
        myFile.write("\n购课时间：\t" + (guide_rel["orderDate"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"))
        select_student_for_studentdatas(guide_rel["student"], guide_rel["subject"])
        select_student_for_studytasks(guide_rel["student"], guide_rel["subject"])


if __name__ == "__main__":
    myFile = open(datetime.datetime.now().strftime("%Y-%m-%d") + "_Info2.txt", "a", encoding='utf-8')
    select_student_for_guider()
    myFile.close()
