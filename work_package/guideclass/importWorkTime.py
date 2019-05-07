from pymongo import MongoClient
import csv
import datetime


def get_mongo():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client = MongoClient(uri)
    collection = client["guideclass_ceshi"]["test"]
    return collection


def WorkTime():
    collect = get_mongo()
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
            collect.insert_one(records)


if __name__ == '__main__':
    print(datetime.datetime.utcnow())
    WorkTime()
