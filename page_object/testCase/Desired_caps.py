# coding:utf-8
import yaml
from appium import webdriver
import logging.config
import os

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


def appium_desired():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(".")))  # 获取当前文件所在目录的上一级目录
    stream = open(root_dir + "/config/desired_caps.yaml", "r")
    data = yaml.load(stream, Loader=yaml.FullLoader)

    desired_caps = {
        "platformName": data["platformName"],
        "platformVersion": data["platformVersion"],
        "deviceName": data["deviceName"],
        "appPackage": data["appPackage"],
        "appActivity": data["appActivity"],
        "unicodeKeyboard": data["unicodeKeyboard"],
        "resetKeyboard": data["resetKeyboard"],
        "noReset": data["noReset"]
    }
    driver = webdriver.Remote("http://" + data["ip"] + ":" + data["port"] + "/wd/hub", desired_caps)
    driver.implicitly_wait(8)
    logs.info("====== start run app ======")
    file_logs.info("====== start run app ======")


if __name__ == '__main__':
    appium_desired()
