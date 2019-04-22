# coding:utf-8
from app_project.businessView.app_login import LoginView
from app_project.testCase.startEnd import StartEnd
import unittest
import logging.config

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class TestLogin(StartEnd):
    csv_file = "../data/loginUser.csv"

    def test_login_https005(self):
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 1)
        test1.login_action(data)

    def test_login_https006(self):
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 2)
        test1.login_action(data)

    @unittest.skip("test_login_https007")
    def test_login_https007(self):
        test1 = LoginView(self.driver)
        data = test1.get_csv_data(self.csv_file, 3)
        test1.login_action(data)


if __name__ == '__main__':
    unittest.main()
