# -*- coding:utf-8 -*-
#
import requests
class UpdateStudentInfo:
    def update_student(self,body,cookie):
        #cookie 从http://172.16.0.210:3030/api/guiderIndexInit接口获取
        uri = "http://172.16.0.210:3030/api/updateStudentInfo"
        resp=requests.post(uri,json=body)
        print(resp.status_code)
        return resp.content.decode("utf-8")
if __name__ == '__main__':
    ust=UpdateStudentInfo()
    body = {"username": "gj235", "realName": "田雅婷", "goHomeFreq": "每天回家", "gradeType": "cz3", "enrollYear": "2015",
            "province": "贵州", "district": "铜仁", "subdistrict": "印江县", "school": "印江县民族中学", "schoolType": "省重点",
            "contactInfo": [{"type": "客户手机号", "value": "13333333333"}, {"type": "家长手机号", "value": "18888888888"},
                            {"type": "家长单位电话", "value": "17777777777"}, {"type": "学生常用", "value": ""},
                            {"type": "家长常用", "value": ""}]}
    ust.update_student(body)
