# coding:utf-8

import unittest
from time import sleep
from app_project.src.util.app_log import my_log
from app_project.src.baseView.desired_caps import devices_start

class StartEnd(unittest.TestCase):
    logger = my_log()

    # @staticmethod
    # def setUpClass(cls):
    #     cls.logger.info("====== setUpClass ======")
    #     pass

    def setUp(self):
        self.logger.info("====== setUp ======")
        self.driver = devices_start()

    def tearDown(self):
        self.logger.info("====== tearDown ======")
        sleep(8)
        self.driver.close_app()

    # @staticmethod
    # def tearDownClass(cls):
    #     cls.logger.info("====== tearDownClass ======")
    #     pass


if __name__ == '__main__':
    unittest.main
