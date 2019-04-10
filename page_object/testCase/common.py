from page_object.testCase.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from page_object.testCase.baseDriver import BaseDriver
import logging.config
from selenium.common.exceptions import NoSuchElementException
from time import sleep

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()
file_logs = logging.getLogger("fileLogger")


class Common(BaseDriver):
    upgrade = (By.ID, "com.guideclasspad:id/cancel_tv")

    def isUpgrade(self):
        try:
            element = self.driver.find_element(*self.upgrade)
        except NoSuchElementException:
            logs.info("=== element is not find===")
            file_logs.info("=== element is not find===")
        else:
            logs.info("=== Undo the upgrade===")
            file_logs.info("=== Undo the upgrade===")
            sleep(5)
            element.click()


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
    com.isUpgrade()
