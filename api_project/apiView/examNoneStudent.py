# -*- coding:utf-8 -*-
#

from api_project.apiView.actionLogin import LoginPage


class ExamNoneStudent:
    def get_ExamNone(self, session, data, ):
        uri = "http://172.16.0.210:3030/api/getExamNoneStudents"
        resp = session.get(url=uri, params=data)
        # print("未首测学员：", resp.status_code)
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
