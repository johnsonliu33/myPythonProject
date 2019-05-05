import datetime

import pymysql
from pymongo import MongoClient


def level_type(vel):
    return {
        0: "同步基础",
        1: "同步提高",
        2: "满分冲刺",
        -1: "-1"
    }.get(vel, "error")  # 'error'为默认返回值


def subject_type(var):
    return {
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
    }.get(var, "学科不存在！")


def time_fmt(times):
    seconds = times / 1000 * 0.8
    m, s = divmod(seconds, 60)
    # h, m = divmod(m, 60)
    return "%02d'%02d\"" % (m, s)


# guideclass
def get_mongodb():
    #uri="mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    uri = "mongodb://dev:dev123@172.16.0.167:27017/guideclass"
    client = MongoClient(uri)
    #guideclass_db = client["guideclass_ceshi"]
    guideclass_db = client["guideclass"]
    return guideclass_db


def get_lesson(sectionid):
    conn=pymysql.connect(host="192.168.1.179",port=3306,user="etwebRead",passwd="etwebRead123",db="easyweb")
    cursor = conn.cursor()
    sql_one = "select lessonguid from W_SectionInfo where guid = '%s' " % sectionid
    res = cursor.execute(sql_one)
    if res > 0:
        for lessionid in cursor.fetchall():
            sql_two = "select lessonname from W_LessonInfo where guid = '%s' " % lessionid
            cursor.execute(sql_two)
            res_lesson = cursor.fetchall()
            # print("\t" + res_lesson[0][0])
            return res_lesson[0][0]
    else:
        return "***lesson为空***"
    cursor.close()
    conn.close()


def get_section(sectionid):
    conn=pymysql.connect(host="192.168.1.179",port=3306,user="etwebRead",passwd="etwebRead123",db="easyweb")
    # conn = pymysql.connect(host="192.168.1.181", port=3306, user="select", passwd="select123", db="easyweb")
    """创建游标"""
    cursor = conn.cursor()
    sql_one = "select sectionname from W_SectionInfo where guid = '%s' " % sectionid
    res = cursor.execute(sql_one)
    if res > 0:
        return cursor.fetchall()[0][0]
    else:
        return "***同类题***"
    cursor.close()
    conn.close()


def get_exam_result(exam_task_id):
    db = get_mongodb()
    exam_result_table = db.examresults
    exam_result_data = exam_result_table.find({"examTaskId": exam_task_id})
    for tasks_two in exam_result_data:
        myFile.write("\n试卷层次 : " + level_type(tasks_two["paperLevel"]))
        myFile.write("\n考试时长 : " + str(tasks_two["costTime"] // 60) + "分钟")
        myFile.write("\n题目数   : " + str(tasks_two["totalNum"]))
        myFile.write("\n做题数   : " + str(tasks_two["submitNum"]))
        myFile.write("\n做错数   : " + str(tasks_two["wrongNum"]))
        myFile.write("\n半对数   : " + str(tasks_two["halfRightNum"]))
        myFile.write("\n正确数   : " + str(tasks_two["rightNum"]))


def get_level(reserveid):
    db = get_mongodb()
    study_statuses_table = db.studystatuses
    study_statuses_data = study_statuses_table.find({"reserveId": reserveid})
    for tasks_three in study_statuses_data:
        for key in tasks_three:
            if key == "levelNew":
                myFile.write("\n下次课层次: " + str(tasks_three["levelNew"]))
            if key == "schoolProgress":
                myFile.write("\n学校学习进度: ")
                myFile.write("\n\t " + str(tasks_three["schoolProgress"]["textbookEdition"]) +
                             "\t " + str(tasks_three["schoolProgress"]["textbook"]) +
                             "\t " + str(tasks_three["schoolProgress"]["chapter"]) +
                             "\t " + str(tasks_three["schoolProgress"]["section"]) +
                             "\t " + str(tasks_three["schoolProgress"]["subsection"]))


def get_study(students, subjects):
    db = get_mongodb()
    study_steps_table = db.studysteps
    study_steps_data = study_steps_table.find({"student": students, "subject": subjects}).sort("listenTime",
                                                                                               -1).limit(
        1)
    for tasks_four in study_steps_data:
        # print(tasks_four["sectionId"] + "  " + tasks_four["lessonId"])
        return tasks_four["sectionId"]


def get_exam_task(students, subjects):
    db = get_mongodb()
    exam_task_table = db.examtasks
    exam_task_data = exam_task_table.find({"student": students, "subject": subjects, "isValid": True})
    print(students + "\t" + subject_type(subjects))
    for tasks_one in exam_task_data:
        play_times = 0
        is_first = "首测" if tasks_one["isFirstExam"] == True else "月测"
        myFile.write(
            "\n===================================================================================================")
        myFile.write("\n学生账号 : " + students)
        myFile.write("\n学    科 : " + subject_type(subjects))
        myFile.write("\n考试类型 : " + is_first)
	
        # print((tasks_one["doTime"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"))
        
        myFile.write(
            "\n考试时间 : " + (tasks_one["doTime"] + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S"))
        myFile.write("\n试卷内容 : ")

        """遍历试卷内容"""
        for i in range(len(tasks_one["paper"]["sections"])):
            temp = (tasks_one["paper"]["sections"])[i]
            if tasks_one["isFirstExam"] == True and "nodeName" in temp.keys():
                p_time = temp["playTime"]
                pt = time_fmt(p_time)
                myFile.write("\n\t" + get_lesson(temp["sectionId"]) + " \t" + temp["nodeName"] + " \t" + pt)
                play_times = play_times + p_time
            elif tasks_one["isFirstExam"] == True and "name" in temp.keys():
                p_time = temp["playTime"]
                pt = time_fmt(p_time)
                myFile.write("\n\t" + get_lesson(temp["sectionId"]) + " \t" + temp["name"] + " \t" + pt)
                play_times = play_times + p_time
            else:
                myFile.write("\n\t" + get_lesson(temp["sectionId"]))

        exam_task_id = tasks_one["id"]
        get_exam_result(exam_task_id)
        reserve_id = tasks_one["reserveId"]
        get_level(reserve_id)
        pts = time_fmt(play_times)
        myFile.write("\n预计做题时长 : " + pts)


def start_select():
    # students = input("请输入查询账号：")
    # students = "PGWZ20, yangan1, QQ1797527728, fahrhggb, Davina0701, wangyuqima, pz2018gy202, zty1105, pz2018gy491, pz2018gy492, pz2018gy493, pz2018gy494, zmhcs, zrzhangrui"
    students = "fyh13611173082, genghao1202, hicihrny, PGWZ20, zty1105, zrzhangrui, pz2018gy202, wz2018gy146, gz13161414192, yichangkongmeng"
    #students = "ifufkdya"
    student_list = students.split(", ")
    subject_list = ["2", "3", "4", "5"]
    #subject_list = "2"
    for stu in student_list:
        for sub in subject_list:
            get_exam_task(stu, sub)
            # sec_id = get_study(stu, sub)
            # myFile.write("\n最后一次学习小节: " + get_lesson(sec_id) + " \t" + get_section(sec_id))
    print("查询完成。。。。。。。。。。。。。")
    # myFile.write("\n\n查询时间: "+ datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+"\n\n")
    # sys.exit()


if __name__ == "__main__":
    myFile = open(datetime.datetime.now().strftime("%Y-%m-%d") + "_studentInfo.txt", "a", encoding='utf-8')
    start_select()
    myFile.close()
