# -*- coding:utf-8 -*-
#
import re
import unittest
from api_project.apiView.updateStudentInfo import UpdateStudentInfo
from api_project.apiView.actionLogin import LoginPage


class TestUpdateStudentInfo(unittest.TestCase):
    def setUp(self):
        print("====== setUp ======")
        loginp = LoginPage()
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        resp=loginp.login_page(body)
        self.session=resp[1]

    def test_exam_true(self):
        ens = UpdateStudentInfo()
        body = {"username": "gj235", "realName": "田雅婷", "goHomeFreq": "每天回家", "gradeType": "cz3", "enrollYear": "2015",
            "province": "贵州", "district": "铜仁", "subdistrict": "印江县", "school": "印江县民族中学", "schoolType": "省重点",
            "contactInfo": [{"type": "客户手机号", "value": "13333333333"}, {"type": "家长手机号", "value": "18888888888"},
                            {"type": "家长单位电话", "value": "17777777777"}, {"type": "学生常用", "value": ""},
                            {"type": "家长常用", "value": ""}]}
        resp = ens.update_student(self.session,body)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    def tearDown(self):
        print("====== tearDown ======")


if __name__ == '__main__':
    unittest.main
