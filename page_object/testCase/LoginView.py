# coding:utf-8
import logging.config
from page_object.testCase.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from page_object.testCase.common import Common

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class LoginView(Common):
    imput_type = (By.CLASS_NAME, "android.widget.EditText")
    login_btn = (By.CLASS_NAME, "android.widget.TextView")

    def login_action(self, usernames, passwords):
        self.isUpgrade()

        imputs = self.driver.find_elements(*self.imput_type)
        logs.info("username:" + usernames)
        file_logs.info("username:" + usernames)
        imputs[0].send_keys(usernames)
        logs.info("passwords:" + passwords)
        file_logs.info("passwords:" + passwords)
        imputs[1].send_keys(passwords)
        button = self.driver.find_element(*self.login_btn)
        button.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = LoginView(driver)
    com.login_action("https005", "11111")
