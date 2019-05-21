# -*- coding:utf-8 -*-
#
import re
import unittest
from api_project.apiView.updateStudentInfo import UpdateStudentInfo
from api_project.apiView.action_login import LoginPage


class TestUpdateStudent(unittest.TestCase):
    def setUp(self):
        print("====== setUp ======")
        loginp = LoginPage()
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        loginp.login_page(body)


    def test_exam_true(self):
        ens = UpdateStudentInfo()
        data = {"guider": "teacherlengjing"}
        resp = ens.get_ExamNone(data)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    def tearDown(self):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main
