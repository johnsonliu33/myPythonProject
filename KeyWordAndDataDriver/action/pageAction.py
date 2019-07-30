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

