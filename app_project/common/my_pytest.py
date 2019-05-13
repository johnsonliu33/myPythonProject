# -*- coding:utf-8 -*-
# coding:utf-8

import pytest
from app_project.baseView.desired_caps import devices_start
from time import sleep
from app_project.common.app_log import my_log


class TestPy:
    logger = my_log()


    @staticmethod
    def setUpClass(cls):
        cls.logger.info("====== setUpClass ======")
        pass

    @pytest.mark.parametrize("uuid")
    def setUp(self):
        self.logger.info("====== setUp ======")
        self.logger.info("uuid=self.uuid")
        self.driver = devices_start(uuid=self.uuid)

    def tearDown(self):
        self.logger.info("====== tearDown ======")
        sleep(8)
        # self.driver.close_app()

    @staticmethod
    def tearDownClass(cls):
        cls.logger.info("====== tearDownClass ======")
        pass


if __name__ == '__main__':
    unittest.main
