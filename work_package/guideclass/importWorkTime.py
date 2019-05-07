from pymongo import MongoClient


def WorkTime():
    uri = "mongodb://guideclass:zaq1xsw2@172.16.0.166:27017/guideclass_ceshi"
    client = MongoClient(uri)
    # collection= client["guideclass_ceshi"]["guiderworktimes"]
    database = client["guideclass_ceshi"]
    collection = database.guiderworktimes

    record_list=[


    ]