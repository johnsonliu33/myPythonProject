# -*- coding:utf-8 -*-
#
import re
import unittest
from api_project.apiView.updateStudentInfo import UpdateStudentInfo
from api_project.apiView.guiderLogin import LoginPage


class TestUpdateStudentInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loginp = LoginPage()
        body = {
            "role": "1",
            "username": "teacherlengjing",
            "password": "11111"
        }
        resp = loginp.login_page(body)
        cls.session = resp[1]

    def test_exam_true1(self):
        """修改学生信息-成功1"""
        ens = UpdateStudentInfo()
        body = {"username": "gj235", "realName": "田雅婷", "goHomeFreq": "每天回家", "gradeType": "cz3", "enrollYear": "2015",
                "province": "贵州", "district": "铜仁", "subdistrict": "印江县", "school": "印江县民族中学", "schoolType": "省重点",
                "contactInfo": [{"type": "客户手机号", "value": "13333333333"}, {"type": "家长手机号", "value": "18888888888"},
                                {"type": "家长单位电话", "value": "17777777777"}, {"type": "学生常用", "value": ""},
                                {"type": "家长常用", "value": ""}]}
        resp = ens.update_student(self.session, body)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    def test_exam_true2(self):
        """修改学生信息-成功2"""
        ens = UpdateStudentInfo()
        body = {"username": "gj235", "realName": "", "goHomeFreq": "", "gradeType": "cz3", "enrollYear": "2015",
                "province": "贵州", "district": "铜仁", "subdistrict": "印江县", "school": "印江县民族中学", "schoolType": "省重点",
                "contactInfo": [{"type": "客户手机号", "value": "13333333333"}, {"type": "家长手机号", "value": "18888888888"},
                                {"type": "家长单位电话", "value": "17777777777"}, {"type": "学生常用", "value": ""},
                                {"type": "家长常用", "value": ""}]}
        resp = ens.update_student(self.session, body)
        key = '"success":(.+?),'
        temp = re.findall(key, resp)
        self.assertEqual(temp[0], "true")

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main
