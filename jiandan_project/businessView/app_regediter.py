# coding=utf-8
import time

from jdkt_package.jdkt_driver import driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random

print("init regedit")
try:
    regedit = driver.find_element_by_id("com.jiandan.mobilelesson:id/regist_btn")
except NoSuchElementException:
    print("no find regedit")
else:
    regedit.click()
    print("to regedit ")


def get_size():
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return x, y


def swipeUp():
    p = get_size()
    x1 = int(p[0] * 0.24)
    y1 = int(p[1] * 0.84)
    y2 = int(p[1] * 0.76)
    driver.swipe(x1, y1, x1, y2, 1000)


def touchUp():
    TouchAction(driver).press(x=150, y=1080).wait(1000).move_to(x=150, y=1180).wait(1000).release().perform()


uname = "jdkt" + str(random.randint(10000, 99999))
username = driver.find_element_by_id("com.jiandan.mobilelesson:id/user_name").send_keys(uname)
passwd = "11111"
password = driver.find_element_by_id("com.jiandan.mobilelesson:id/password").send_keys(passwd)

# x:180 y:1080 press:100
driver.find_element_by_id("com.jiandan.mobilelesson:id/gradetv").click()
time.sleep(1)
swipeUp()

driver.find_element_by_id("com.jiandan.mobilelesson:id/grade").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/year").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/confirm").click()

driver.find_element_by_id("com.jiandan.mobilelesson:id/school").click()
time.sleep(1)
touchUp()

driver.find_element_by_id("com.jiandan.mobilelesson:id/province").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/city").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/district").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/confirm").click()

iphone = "13344" + str(random.randint(100000, 999999))
driver.find_element_by_id("com.jiandan.mobilelesson:id/cellphone").send_keys(iphone)
driver.find_element_by_id("com.jiandan.mobilelesson:id/getcheckcode").click()

# driver.get_screenshot_as_file("./image/valid.png")
mobile_message = r"验证码已发送到您的手机"
message1 = '//*[@text=\'{}\']'.format(mobile_message)
try:
    toast_element1 = WebDriverWait(driver, 8, 0.01).until(EC.presence_of_element_located(By.xpath(message1)))
except:
    driver.get_screenshot_as_file("./image/valid_error.png")
else:
    print(toast_element1.text)

driver.find_element_by_id("com.jiandan.mobilelesson:id/checkcode").send_keys("123456")
driver.find_element_by_id("com.jiandan.mobilelesson:id/use_regist").click()
# driver.get_screenshot_as_file("./image/toast.png")
error_message = r"短信验证码错误"
message2 = '//*[@text=\'{}\']'.format(error_message)
try:
    toast_element2 = WebDriverWait(driver, 8, 0.01).until(lambda x: x.find_element_by_xpath(message2))
except:
    driver.get_screenshot_as_file("./image/toast_error.png")
else:
    print(toast_element2.text)
