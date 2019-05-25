# -*- coding:utf-8 -*-
#
import os
import yaml
from api_project.apiView.guiderLogin import LoginPage


class UpdateStudentInfo:
    def __init__(self):
        file_path = os.path.dirname(os.path.dirname(__file__))
        with open(file_path + "/config/host.yaml", "r", encoding="utf-8") as file:
            self.host = yaml.full_load(file)

    def update_student(self, session, body):
        uri = "http://" + self.host["host"] + ":3030" + "/api/updateStudentInfo"
        resp = session.post(uri, data=body)
        # print("更新学生信息：", resp.status_code)
        return resp.content.decode("utf-8")


if __name__ == '__main__':
    loginp = LoginPage()
    body = {
        "role": "1",
        "username": "teacherlengjing",
        "password": "11111"
    }
    session = loginp.login_page(body)[1]
    ust = UpdateStudentInfo()
    body = {"username": "gj235", "realName": "田雅婷", "goHomeFreq": "每天回家", "gradeType": "cz3", "enrollYear": "2015",
            "province": "贵州", "district": "铜仁", "subdistrict": "印江县", "school": "印江县民族中学", "schoolType": "省重点",
            "contactInfo": [{"type": "客户手机号", "value": "13333333333"}, {"type": "家长手机号", "value": "18888888888"},
                            {"type": "家长单位电话", "value": "17777777777"}, {"type": "学生常用", "value": ""},
                            {"type": "家长常用", "value": ""}]}
    ust.update_student(session, body)
