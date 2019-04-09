# coding:utf-8
import logging.config
from page_object.testCase.Desired_caps import appium_desired
from selenium.webdriver.common.by import By
from page_object.testCase.BaseDriver import BaseDriver

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class LoginView():
    username_type = (By.ID, "com.jiandan.mobilelesson:id/account_et")
    password_type = (By.ID, "com.jiandan.mobilelesson:id/password_et")
    login_btn = (By.ID, "com.jiandan.mobilelesson:id/login_btn")

    def login_action(self, usernames, passwords):
        username = self.driver.find_element(*self.username_type)
        username.clear()
        username.send_keys(usernames)
        password = self.driver.find_element(*self.password_type)
        password.send_keys(passwords)
        button = self.driver.find_element(*self.login_btn)
        button.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = LoginView(driver)
    com.login_action("https005", "11111")
