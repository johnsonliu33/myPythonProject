# -*- coding:utf-8 -*-
import time

from util.objectMap import *
from util.keyBoardUtil import KeyBoardKeys
from util.clipboardUtil import Clipboard
from util.waitUtil import WaitUtil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def TestSendMailAndAttachment():
    driver = webdriver.Chrome(executable_path="./../driver/chromedriver.exe")
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
    newContact = getElements(driver,"link text", "新建联系人")
    newContact[1].click()
    contactName = wait_util.visibilityOfElementLocated("id", "_mail_input_7_366")
    contactName.send_keys("test")
    newEmail = wait_util.visibilityOfElementLocated("xpath", '//*[@id="_mail_input_8_369"]/input')
    newEmail.send_keys("779446928@qq.com")
    getElement(driver, "xpath", '//*[@id="_mail_button_37_484"]/span').click()
    assert "test" in driver.page_source
    print("添加联系人成功")



    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    TestSendMailAndAttachment()
