# -*- coding:utf-8 -*-
import requests
import unittest
import yaml
from api.test_package.mysql_action import MysqlDB


class TestUser(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/users"
        self.auth = ("admin", "123456")

    def test_get_user(self):
        """验证user1存在"""
        resp = requests.get(url=self.base_url + "/1/", auth=self.auth)
        result = resp.json()
        self.assertEqual(result["username"], "user1")
        self.assertEqual(result["email"], "123456@163.com")


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/groups"
        self.auth = ("admin", "123456")

    def test_get_group(self):
        """验证group1存在"""
        resp = requests.get(url=self.base_url + "/1/", auth=self.auth)
        result = resp.json()
        self.assertEqual(result["name"], "group1")


if __name__ == '__main__':
    db = MysqlDB()
    f = open("datas.yaml", "r")
    datas = yaml.full_load(f)
    db.init_data(f)
    unittest.main()
