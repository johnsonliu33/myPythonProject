from jiandan_project.baseView.baseDriver import BaseDriver
from jiandan_project.baseView.desired_caps import appium_desired
import logging.config

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()


class Common(BaseDriver):

    def common_fun(self):
        logs.info("====== common_function ======")


if __name__ == '__main__':
    driver = appium_desired()
    c = Common(driver)
    c.common_function()
