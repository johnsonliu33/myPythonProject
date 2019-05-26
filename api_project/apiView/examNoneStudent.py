# -*- coding:utf-8 -*-
#
import os
import yaml
from api_project.apiView.guiderLogin import LoginPage


class ExamNoneStudent:
    def __init__(self):
        file_path = os.path.dirname(os.path.dirname(__file__))
        with open(file_path + "/config/host.yaml", "r", encoding="utf-8") as file:
            self.host = yaml.full_load(file)

    def get_ExamNone(self, session, data, ):
        uri = "http://" + self.host["host"] + ":3030" + "/api/getExamNoneStudents"
        resp = session.get(url=uri, params=data)
        return resp.content.decode("utf-8")


if __name__ == '__main__':
    loginp = LoginPage()
    body = {
        "role": "1",
        "username": "teacherlengjing",
        "password": "11111"
    }
    session = loginp.login_page(body)[1]
    ens = ExamNoneStudent()
    data = {"guider": "teacherlengjing"}
    r = ens.get_ExamNone(session, data)
