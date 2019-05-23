# -*- coding:utf-8 -*-
#
import unittest
import re
from api_project.apiView.actionLogin import LoginPage
from api_project.apiView.examNoneStudent import ExamNoneStudent


class Test_ExamNoneStudent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("====== setUp ======")
        loginp = LoginPage()
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        resp = loginp.login_page(body)
        cls.session = resp[1]

    def test_exam_true(self):
        """未定首测学员"""
        ens = ExamNoneStudent()
        data = {"guider": "teacherlengjing"}
        resp = ens.get_ExamNone(self.session, data)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    @classmethod
    def tearDownClass(cls):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main
