# -*- coding:utf-8 -*-
#
import unittest
import re
from api_project.apiView.action_login import LoginPage
from api_project.apiView.examNoneStudent import ExamNoneStudent


class Test_ExamNone(unittest.TestCase):
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
        ens = ExamNoneStudent()
        data = {"guider": "teacherlengjing"}
        resp = ens.get_ExamNone(data)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    def tearDown(self):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main
