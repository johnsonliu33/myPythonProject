import xlrd
import datetime
from pymongo import MongoClient, errors


def get_mongo_db():
    DATABASE = "guideclass_ceshi2"
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/{}".format(
        DATABASE)
    client = MongoClient(uri)
    db = client[DATABASE]
    return db


def get_seqidgens_collect(collect):
    return collect["seqidgens"]


def get_meetingtimes_collect(collect):
    # return collect["meetingtimes"]
    return collect["test"]


def get_id(collect, user, init=123):
    # $inc:   ({"_id": "meetingTimeId"},{$inc:{"seq":1}})   -- 找到id是meetingTimeId的数据，把seq参数加1
    # $set:   ({"_id": "meetingTimeId"},{$set:{"temp":"更新"}}) -- 找到id是meetingTimeId的数据，更新updatedAt时间为当前时间
    # upsert=true时，匹配不到数据会插入一条新数据
    getRes = collect.find_one_and_update({"_id": user}, {"$inc": {"seq": 1}, "$set": {
        "updatedAt": datetime.datetime.utcnow()}}, new=True, upsert=True, setDefaultsOnInsert=True)
    if getRes and (getRes["seq"] < init):
        getRes = collect.find_one_and_update({"_id": user},
                                             {"$inc": {"seq": init}, "$set": {
                                                 "updatedAt": datetime.datetime.utcnow()}},
                                             new=True, upsert=True, setDefaultsOnInsert=True)
    return getRes["seq"]


def create_id(sid):
    return "mt_" + str(sid)


def guide_type_dict(var):
    return {
        "初一": "cz1",
        "初二": "cz2",
        "初三": "cz3",
        "六年级": "6",
        "七年级": "7",
        "八年级": "8",
        "九年级": "9",
        "高一": "gz1",
        "高二": "gz2",
        "高三": "gz3",
        "初中": "cz1,cz2,cz3,6,7,8,9",
        "高中": "gz1,gz2,gz3",
    }.get(var, "guide is not find")


def format_guide_type_list(guide_type_list):
    # 年级转换成['cz1','cz2','cz3','6','7','8','9','gz1','gz2','gz3']并去重
    if guide_type_list is None:
        print("guide_type_list is none")
        return None
    gts = []
    for item_list in guide_type_list:
        item_list = item_list.strip()
        item = guide_type_dict(item_list).split(",")
        gts.extend(item)
    gts = list(set(gts))
    gts.sort()
    return gts


def utc_date_time(book_datemode, date_value, time_value):
    # date和time转换成datetime格式
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
        time2 = xlrd.xldate_as_tuple(time_value, book_datemode)
        hour = time2[3:][0]
        minute = time2[3:][1]
    date_time = datetime.datetime(
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        0)
    utc_date_time = date_time + datetime.timedelta(hours=-8)
    return utc_date_time


# exec()用来执行储存在字符串或文件中的Python语句,支持Python代码的动态执行
def exec(meetingtimes_collect, seqidgens_collect):
    book = xlrd.open_workbook("demo-直播班会时间安排.xlsx")
    sheet = book.sheet_by_index(0)
    col_num = sheet.nrows
    valid_num = 0
    insert_num = 0
    for i in range(1, col_num):
        # 过滤年级为空的情况
        grade = sheet.cell_value(i, 2)
        if grade == "" or grade == "年级":
            continue
        date_value = sheet.cell_value(i, 1)
        guide_type = sheet.cell_value(i, 2)
        guide_type_before_list = guide_type.split("、")
        guide_type_after_list = format_guide_type_list(guide_type_before_list)
        time_value = sheet.cell_value(i, 3)
        guide_username = sheet.cell_value(i, 4)
        book_datemode = book.datemode
        utc_meeting_date = utc_date_time(book_datemode, date_value, time_value)
        create_id(get_id(seqidgens_collect, "meetingTimeId", 1000000)),
        records = {
            "isValid": True,
            "classTime": utc_meeting_date,
            "duration": 30,
            "gradeType": guide_type_after_list,
            "guider": guide_username,
            "createdAt": datetime.datetime.utcnow(),
            "updatedAt": datetime.datetime.utcnow()
        }
        print(records)
        valid_num += 1
        try:
            meetingtimes_collect.insert_one(records)
        except Exception as e:
            print(e)
        else:
            insert_num += 1
    ############################################
    ############################################
    print("=" * 10)
    print("=插入数据为: %s 条=" % insert_num)
    print("=" * 10)
    print("=有效数据为: %s 条=" % valid_num)


if __name__ == "__main__":
    db = get_mongo_db()
    exec(get_meetingtimes_collect(db), get_seqidgens_collect(db))
