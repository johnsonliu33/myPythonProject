from pymongo import MongoClient
import csv
import datetime


def get_mongo():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client = MongoClient(uri)
    dataBase = client["guideclass_ceshi"]
    return dataBase


def WorkTime():
    dataBase = get_mongo()
    collection = dataBase.guiderworktimes
    with open("worktime.csv", "r") as file:
        data_list = csv.reader(file)
        for row in data_list:
            print(row)
            item = row[0].split("/")
            year = int(item[0])
            month = int(item[1])
            day = int(item[2])
            # print(year,month,day)
            records = {
                "date": datetime.datetime(year, month, day),
                "guider": row[1],
                "__v": 0,
                "createdAt": datetime.datetime.utcnow(),
                "time": row[2],
                "updatedAt": datetime.datetime.utcnow()
            }
            collection.insert_one(records)


def MeetTime():
    dataBase = get_mongo()
    collection = dataBase.meetingtimes
    with open("meettime.csv", "r") as file:
        data_list = csv.reader(file)
        for row in data_list:
            print(row)
            item = row[1].split(" ")
            dates = item[0].split("/")
            times = item[1].split(":")
            year = int(dates[0])
            month = int(dates[1])
            day = int(dates[2])
            hour = int(times[0])
            minute = int(times[1])
            second = int(times[2])
            records = {
                "isValid": "true",
                "guider": row[0],
                "classTime": datetime.datetime(year, month, day, hour, minute, second),
                "duration": row[2],
                "textDesc": row[3],
                "id": row[4],
                "createdAt": datetime.datetime.utcnow(),
                "updatedAt": datetime.datetime.utcnow(),
                "__v": 0
            }
            collection.insert_one(records)


if __name__ == '__main__':
    print(datetime.datetime.utcnow())
    # WorkTime()
    MeetTime()
