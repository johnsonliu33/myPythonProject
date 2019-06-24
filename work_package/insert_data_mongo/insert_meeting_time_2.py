import xlrd
import datetime
from pymongo import MongoClient,errors


def get_mongo():
    DATABASE = "guideclass_ceshi2"
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/{}".format(DATABASE)
    client = MongoClient(uri)
    collection = client[DATABASE]
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
    if getRes and (getRes["seq"] < init):
        getRes = collect.find_one_and_update({"_id": user},
                                             {"$inc": {"seq": init}, "$set": {"updatedAt": datetime.datetime.utcnow()}},
                                             new=True, upsert=True, setDefaultsOnInsert=True)
    return getRes["seq"]


def create_id(sid):
    return "mt_" + str(sid)


def utc_dateTime(book_datemode, date_value, time_value):
    if isinstance(date_value, str):
        date1 = date_value.split("/")
        year = date1[0]
        month = date1[1]
        day = date1[2]
    else:
        # book.datemode 以日期方式显示该单元数据
        date2 = xlrd.xldate_as_tuple(date_value, book_datemode)
        year = date2[:3][0]
        month = date2[:3][1]
        day = date2[:3][2]
    if isinstance(time_value, str):
        time1 = time_value.split(":")
        hour = time1[0]
        minute = time1[1]
    else:
        time2 = xlrd.xldate_as_tuple(date_value, book_datemode)
        hour = time2[3:][0]
        minute = time2[3:][1]
    date_time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 0)
    utc_date_time = date_time + datetime.timedelta(hours=-8)
    return utc_date_time


# exec()用来执行储存在字符串或文件中的Python语句,支持Python代码的动态执行
def exec(meetingtimes_collect, seqidgens_collect):
    book = xlrd.open_workbook("班会时间安排 -衡水荣春波.xlsx")
    sheet = book.sheet_by_index(0)
    colnum = sheet.nrows
    valid_num = 0
    insert_num = 0
    for i in range(1, colnum):
        # 过滤年级为空的情况
        grade = sheet.cell_value(i, 2)
        if grade == "" or grade == "年级":
            continue
        date_value = sheet.cell_value(i, 1)
        time_value = sheet.cell_value(i, 3)
        guide_username= sheet._cell_values(i,4)
        book_datemode = book.datemode
        utc_meeting_date = utc_dateTime(book_datemode, date_value, time_value)
        gradeType = "cz" if grade == "初中" else "gz"
        create_id(get_id(seqidgens_collect, "meetingTimeId", 1000000)),
        records = {
            "isValid": True,
            "classTime": utc_meeting_date,
            "duration": 30,
            "gradeType": gradeType,
            "guider":guide_username,
            "createdAt": datetime.datetime.utcnow(),
            "updatedAt": datetime.datetime.utcnow()
        }
        valid_num += 1
        try:
            meetingtimes_collect.insert_one(records)
        except errors.DuplicateKeyError as e:
            print(e)
        else:
            insert_num += 1
    ############################################
    ############################################

    print("===================")
    print("=有效数据为: " + str(valid_num) + " 条=")
    print("=插入数据为: " + str(insert_num) + " 条=")
    print("===================")


if __name__ == "__main__":
    collect = get_mongo()
    exec(get_meetingtimes_collect(collect), get_seqidgens_collect(collect))
