# -*- coding:utf-8 -*-
from src.businessView.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class LoginView(BasePage):
    api = "/pro/user-login-L3Byby8=.html"
    # 定位器
    username_loc = (By.NAME, "account")
    password_loc = (By.NAME, "password")
    submit_loc = (By.ID, "submit")

    def type_username(self, username):
        self.get_element(*self.username_loc).clear()
        self.get_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.get_element(*self.password_loc).clear()
        self.get_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.get_element(*self.submit_loc).click()

    def test_user_login(b_driver, username, password):
        viewlogin = LoginView(b_driver)
        viewlogin.open(viewlogin.api)
        viewlogin.type_username(username)
        viewlogin.type_password(password)
        viewlogin.type_submit()
        sleep(3)

