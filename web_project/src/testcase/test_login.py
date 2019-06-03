# -*- coding:utf-8 -*-
from time import sleep
from web_project.src.baseview.index_view import IndexView
from web_project.src.baseview.login_view import LoginView
from selenium import webdriver

driver=webdriver.Firefox()

username="admin"
password="Mm123456"
IndexView.test_zt_type(driver)
LoginView.test_user_login(driver,username,password)
sleep(3)
driver.quit()