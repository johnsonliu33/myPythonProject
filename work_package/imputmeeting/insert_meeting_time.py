import xlrd
import datetime
from pymongo import MongoClient


def get_mongo():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client = MongoClient(uri)
    collection = client["guideclass_ceshi"]
    return collection


def get_seqidgens_collect(collect):
    return collect["seqidgens"]


def get_meetingtimes_collect(collect):
    return collect["meetingtimes"]
    # return collect["test"]


def get_id(collect, user, init=123):
    # $inc:   ({"_id": "meetingTimeId"},{$inc:{"seq":1}})   -- 找到id是meetingTimeId的数据，把seq参数加1
    # $set:   ({"_id": "meetingTimeId"},{$set:{"temp":"更新"}}) -- 找到id是meetingTimeId的数据，更新updatedAt时间为当前时间
    # upsert=true时，匹配不到数据会插入一条新数据
    getRes = collect.find_one_and_update({"_id": user}, {"$inc": {"seq": 1}, "$set": {
        "updatedAt": datetime.datetime.utcnow()}}, new=True, upsert=True, setDefaultsOnInsert=True)
    print("getRes===",getRes)
    if getRes and (getRes["seq"] < init):
        getRes = collect.find_one_and_update({"_id": user},
                                             {"$inc": {"seq": init}, "$set": {"updatedAt": datetime.datetime.utcnow()}},
                                             new=True, upsert=True, setDefaultsOnInsert=True)

    return getRes["seq"]


def create_id(sid):
    return "mt_" + str(sid)

# exec()用来执行储存在字符串或文件中的Python语句,支持Python代码的动态执行
def exec(meetingtimes_collect, seqidgens_collect):
    book = xlrd.open_workbook("直播班会时间安排.xlsx")

    sheet = book.sheet_by_index(0)
    colnum = sheet.nrows
    valid_num = 0

    for i in range(1, colnum):

        # 过滤年级为空的情况
        grade = sheet.cell_value(i, 2)
        if grade == "":
            continue

        valid_num += 1
        # book.datemode 以日期方式显示该单元数据
        date_value = xlrd.xldate_as_tuple(sheet.cell_value(i, 1), book.datemode)
        time_value = xlrd.xldate_as_tuple(sheet.cell_value(i, 3), book.datemode)
        meeting_date = datetime.datetime(date_value[:3][0], date_value[:3][1], date_value[:3][2], time_value[3:][0],
                                         time_value[3:][1], time_value[3:][2])

        gradeType = ""

        if grade == "初中":
            gradeType = "cz"
        else:
            gradeType = "gz"
        records = {
            "id": create_id(get_id(seqidgens_collect, "meetingTimeId", 1000000)),
            "isValid": True,
            "classTime": meeting_date,
            "duration": 30,
            "gradeType": gradeType,
            "createdAt": datetime.datetime.utcnow(),
            "updatedAt": datetime.datetime.utcnow()
        }
        meetingtimes_collect.insert_one(records)

    ############################################
    ############################################
    print("===================")
    print("=有效数据为: " + str(valid_num) + " 条=")
    print("===================")


if __name__ == "__main__":
    collect = get_mongo()
    exec(get_meetingtimes_collect(collect), get_seqidgens_collect(collect))
