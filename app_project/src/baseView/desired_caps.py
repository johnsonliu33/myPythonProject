# adb connect 127.0.0.1:62025
# -*- coding:utf-8 -*-
import os
from time import strftime

import yaml
from app_project.src.common.testUpgrade import IsUpgrade
from appium import webdriver

from app_project.src.baseView.multi_appium import appium_start
from app_project.src.util.app_log import my_log


def get_desired(yamlName):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    with open(root_dir + "/config/" + yamlName + ".yaml", "r", encoding="utf-8") as file:
        desired = yaml.load(file, Loader=yaml.FullLoader)
    return desired


def devices_start():
    logger = my_log()
    desired = get_desired(uuid)
    if appium_start(desired["host"], int(desired["port"])):
        _desired_caps = {
            "platformName": desired["platformName"],
            "platformVersion": desired["platformVersion"],
            "deviceName": uuid,
            "appPackage": desired["appPackage"],
            "appActivity": desired["appActivity"],
            "unicodeKeyboard": desired["unicodeKeyboard"],
            "resetKeyboard": desired["resetKeyboard"],
            "noReset": desired["noReset"]
        }
        try:
            logger.info("appium port : {} start run {} at {} ".format(desired["port"], desired["deviceName"],
                                                                      strftime("%Y-%m-%d %H:%M:%S")))
            driver = webdriver.Remote("http://" + desired["host"] + ":" + desired["port"] + "/wd/hub", _desired_caps)
            driver.implicitly_wait(8)
            logger.info("====== start run app : {}======".format(desired["deviceName"]))
            isupg = IsUpgrade(driver)
            isupg.is_upgrade()
            return driver
        except:
            logger.error("appium port : {} start Failed {} at {} ".format(desired["port"], desired["deviceName"],
                                                                          strftime("%Y-%m-%d %H:%M:%S")))


if __name__ == "__main__":
    devices_list = ["desired_cap"]
    devices_start(devices_list[0])
