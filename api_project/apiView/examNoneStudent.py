# -*- coding:utf-8 -*-
#
import requests


class ExamNoneStudent:
    def get_ExamNone(self, data):
        uri = "http://172.16.0.210:3030/api/getExamNoneStudents"
        resp = requests.get(url=uri, params=data)
        print("未首测学员：", resp.status_code)
        return resp.content.decode("utf-8")

if __name__ == '__main__':
    ens=ExamNoneStudent()
    data={"guider": "teacherlengjing"}
    r=ens.get_ExamNone(data)