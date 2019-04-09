# coding:utf-8
from page_object.testCase.LoginView import LoginView
from page_object.testCase.StartEnd import StartEnd
import unittest
import logging.config

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class TestLogin(StartEnd):

    def test_login_https005(self):
        test1 = LoginView(self.driver)
        test1.login_action("https005", "11111")

    def test_login_https006(self):
        test1 = LoginView(self.driver)
        test1.login_action("https006", "11111")

    def test_login_https007(self):
        test1 = LoginView(self.driver)
        test1.login_action("https007", "111111")


if __name__ == '__main__':
    unittest.main()
