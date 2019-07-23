import xlrd
import datetime
from pymongo import MongoClient
import os
import logging

now_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# 初始化日志对象
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(asctime)s %(filename)s[line:%(lineno)d] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=r"D:\学管师排班\%s_logs.log" % now_time,
    filemode="w"
)


def get_mongo_db():
    DATABASE = "guideclass_ceshi"
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/{}".format(
        DATABASE)
    client = MongoClient(uri)
    db = client[DATABASE]
    return db


def get_seqidgens_collect(collect):
    return collect["seqidgens"]


def get_meetingtimes_collect(collect):
    return collect["meetingtimes_copy1"]
    # return collect["test"]


def get_id(collect, user, init=123):
    # $inc:   ({"_id": "meetingTimeId"},{$inc:{"seq":1}})   -- 找到id是meetingTimeId的数据，把seq参数加1
    # $set:   ({"_id": "meetingTimeId"},{$set:{"updatedAt":datetime.datetime.utcnow()}}) -- 找到id是meetingTimeId的数据，更新updatedAt时间为当前时间
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
        "初一": "初一",
        "初二": "初二",
        "初三": "初三",
        "六年级": "六年级",
        "七年级": "七年级",
        "八年级": "八年级",
        "九年级": "九年级",
        "高一": "高一",
        "高二": "高二",
        "高三": "高三",
        "初中": "初一,初二,初三,六年级,七年级,八年级,九年级",
        "高中": "高一,高二,高三",
        "初高中":"初一,初二,初三,六年级,七年级,八年级,九年级,高一,高二,高三"
    }.get(var, None)


def format_guide_type_list(guide_type_list):
    # 年级转换成['cz1','cz2','cz3','6','7','8','9','gz1','gz2','gz3']并去重
    if guide_type_list is None:
        print("guide_type_list is None")
        logging.error("guide_type_list is None")
        return None
    gts = []
    for item_list in guide_type_list:
        item_list = item_list.strip()
        if guide_type_dict(item_list) is not None:
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
def exec(meetingtimes_collect, seqidgens_collect, xlsx_name):
    # book = xlrd.open_workbook("demo-直播班会时间安排.xlsx")
    book = xlrd.open_workbook(xlsx_name)
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
        if date_value is None:
            continue
        guide_type = sheet.cell_value(i, 2)
        guide_type_before_list = guide_type.split("、")
        guide_type_after_list = format_guide_type_list(guide_type_before_list)
        if len(guide_type_after_list) == 0:
            continue
        time_value = sheet.cell_value(i, 3)
        if time_value is None:
            continue
        guide_username = sheet.cell_value(i, 4)
        # guide_username = "xueguanshi60"
        if guide_username is None:
            continue
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
        logging.info(records)
        valid_num += 1
        try:
            meetingtimes_collect.insert_one(records)
        except Exception as e:
            print(e)
            logging.error(e)
        else:
            insert_num += 1
    ############################################
    ############################################
    print("=" * 10)
    logging.info("=" * 10)
    print(file_name + "=插入数据为: %s 条=" % insert_num)
    logging.info(file_name + "=插入数据为: %s 条=" % insert_num)
    print("=" * 10)
    logging.info("=" * 10)
    print(file_name + "=有效数据为: %s 条=" % valid_num)
    logging.info(file_name + "=有效数据为: %s 条=" % valid_num)
    logging.info("=" * 10)


if __name__ == "__main__":
    db = get_mongo_db()
    dir_name = r"D:\学管师排班"
    dir_list = os.listdir(dir_name)
    for child_name in dir_list:
        if child_name.endswith(".xlsx") or child_name.endswith(".xls"):
            file_name = os.path.join(dir_name, child_name)
            exec(
                get_meetingtimes_collect(db),
                get_seqidgens_collect(db),
                file_name)
