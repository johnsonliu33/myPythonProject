# -*- coding:utf-8 -*-
from selenium import webdriver
from config.varConfig import ieDriverFilePath
from config.varConfig import chromeDriverFilePath
from config.varConfig import firefoxDriverFilePath
from util.objectMap import getElement
from util.clipboardUtil import Clipboard
from util.keyBoardUtil import KeyBoardKeys
from util.dirAndTime import *
from util.waitUtil import WaitUtil
from selenium.webdriver.chrome.options import Options
import time

driver = None
waitUtil=None

def open_browser(browserName,*args):
    global driver,waitUtil
    try:
        if browserName.lower() == "ie":
            driver= webdriver.Ie(executable_path=ieDriverFilePath)
        elif browserName.lower()=="chrome":
            driver = webdriver.Chrome(executable_path=chromeDriverFilePath)
            chrome_options=Options()
        else:
            driver = webdriver.Firefox(executable_path=firefoxDriverFilePath)
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e