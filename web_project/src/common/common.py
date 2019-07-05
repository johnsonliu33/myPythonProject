# -*- coding:utf-8 -*-
import os
from selenium import webdriver


def save_img(driver, img_name):
    dir_path = os.path.dirname(os.path.dirname(__file__))
    img_path = os.path.join(dir_path, "report", "screenShot", img_name)
    print(img_path)
    driver.get_screenshot_as_file(img_path)


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="../../driver/geckodriver.exe")
    driver.get("http://www.baidu.com")
    save_img(driver, "../../logs/baidu.png")
    driver.quit()
