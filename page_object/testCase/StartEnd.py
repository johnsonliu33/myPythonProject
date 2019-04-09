# coding:utf-8

import unittest
from page_object.testCase.Desired_caps import appium_desired
import logging.config
from time import sleep

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class StartEnd(unittest.TestCase):

    def setUp(self):
        logs.info("======setUp=========")
        self.driver = appium_desired()

    def tearDown(self):
        logs.info("======tearDown=========")
        sleep(5)
        self.driver.close_app()
