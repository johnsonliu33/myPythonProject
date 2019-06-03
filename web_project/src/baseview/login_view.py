# -*- coding:utf-8 -*-
from web_project.src.basepage.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginView(BasePage):
    api = "/pro/user-login-L3Byby8=.html"
    # 定位器
    username_loc = (By.NAME, "account")
    password_loc = (By.NAME, "password")
    submit_loc = (By.ID, "submit")

    def type_username(self, username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    def test_user_login(driver, username, password):
        viewlogin = LoginView(driver)
        viewlogin.open(viewlogin.api)
        viewlogin.type_username(username)
        viewlogin.type_password(password)
        viewlogin.type_submit()
