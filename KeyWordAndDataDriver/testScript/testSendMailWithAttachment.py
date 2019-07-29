# -*- coding:utf-8 -*-
import time

from util.objectMap import *
from util.keyBoardUtil import KeyBoardKeys
from util.clipboardUtil import Clipboard
from util.waitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config.varConfig import chromeDriverFilePath


def TestSendMailAndAttachment():
    driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
    driver.maximize_window()
    print("启动浏览器成功")
    driver.get("http://mail.163.com")
    time.sleep(3)
    assert "163网易免费邮" in driver.title
    print("访问163登录页面成功")

    wait_util = WaitUtil(driver)

    login = getElement(driver, "id", "lbNormal")
    login.click()
    wait_util.frameToBeAvailableAndSwitchToIt("tag_name", 'iframe')
    username = getElement(driver, "name", "email")
    username.send_keys("15510099753")
    password = getElement(driver, "name", "password")
    password.send_keys("Sq121314")
    # password.send_keys(Keys.ENTER)
    butten = getElement(driver, "id", "dologin")
    butten.click()
    time.sleep(3)
    assert "未读邮件" in driver.page_source
    print("登录成功")
    addressBook = wait_util.visibilityOfElementLocated("xpath", '//*[@id="_mail_tabitem_1_4"]')
    addressBook.click()
    print("通讯录")
    newContact = wait_util.visibilityOfElementLocated("xpath", '//span[text()="新建联系人"]')
    newContact.click()
    print("新建联系人")
    contactName = wait_util.visibilityOfElementLocated("id", "input_N")
    contactName.send_keys("test")
    print("姓名")
    newEmail = wait_util.visibilityOfElementLocated("xpath", '//*[@id="iaddress_MAIL_wrap"]//input')
    newEmail.send_keys("779446928@qq.com")
    print("邮箱")
    getElement(driver, "xpath", '//span[text()="确 定"]').click()
    assert "779446928@qq.com" in driver.page_source
    print("添加联系人成功")

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    TestSendMailAndAttachment()
