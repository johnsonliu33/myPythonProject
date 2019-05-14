# coding:utf-8
import unittest

from app_project.src.common.myUnittest import StartEnd

from app_project.src.businessView.app_login import LoginView
from app_project.src.util.app_log import my_log


class TestLogin(StartEnd):
    logger = my_log()
    csv_file = "../data/loginUser.csv"

    def test_login_https005(self):
        """登录测试"""
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 1)
        test1.login_action(data)

    def test_login_https006(self):
        """登录测试"""
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 2)
        test1.login_action(data)

    @unittest.skip("test_login_https007")  # 跳过
    def test_login_https007(self):
        """登录测试"""
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 3)
        test1.login_action(data)


if __name__ == '__main__':
    unittest.main()
