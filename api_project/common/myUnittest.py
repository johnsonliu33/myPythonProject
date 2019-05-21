# coding:utf-8
import re
import unittest
from api_project.apiView.HomePage import HomePage

class StartEnd(unittest.TestCase):
    # @staticmethod
    # def setUpClass(cls):
    #     pass

    def setUp(self):
        print("====== setUp ======")
        start=HomePage()
        cont=start.home_page()
        key="<title>(.+?)</title>"
        temp = re.findall(key, cont)
        print(temp)
        self.assertEqual(temp[0],"用户登录")

    def tearDown(self):
        print("====== tearDown ======")

    # @staticmethod
    # def tearDownClass(cls):
    #     pass


if __name__ == '__main__':
    unittest.main
