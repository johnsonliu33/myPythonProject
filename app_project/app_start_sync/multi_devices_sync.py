# adb connect 127.0.0.1:62025
# -*- coding:utf-8 -*-
import os
from multiprocessing import Process
from time import strftime

import yaml
from appium import webdriver

from app_project.src.baseView.appium_start import appium_start
from app_project.src.util.app_log import my_log


def get_desired(yamlName):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    with open(root_dir + "/config/desired_caps/" + yamlName + ".yaml", "r", encoding="utf-8") as file:
        desired = yaml.load(file, Loader=yaml.FullLoader)
        # 或者 desired = yaml.full_load(file)
    return desired


def devices_start(devices):
    logger = my_log()
    desired = get_desired(devices)
    if appium_start(desired["host"], int(desired["port"])):
        _desired_caps = {
            "platformName": desired["platformName"],
            "platformVersion": desired["platformVersion"],
            "deviceName": desired["deviceName"],
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
            return driver
        except:
            logger.error("appium port : {} start Failed {} at {} ".format(desired["port"], desired["deviceName"],
                                                                          strftime("%Y-%m-%d %H:%M:%S")))


def multi_devices(devices_list):
    # 构建进程组
    devices_pocess = []
    # 加载desired进程
    for i in range(len(devices_list)):
        # port = 4723 + 2 * i
        devices = Process(target=devices_start, args=(devices_list[i],))
        devices_pocess.append(devices)
    for dps in devices_pocess:
        dps.start()
    for dps in devices_pocess:
        dps.join()


if __name__ == "__main__":
    devices_list = ["62001", "62025"]
    multi_devices(devices_list)
