# -*- coding:utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from app_project.common.app_common import Common


class IsUpgrade(Common):
    def __init__(self, driver):
        self.driver = driver
        self.upgrade = (By.ID, "com.guideclasspad:id/cancel_tv")

    # 取消升级
    def is_upgrade(self):
        self.logger.info("is_upgrade")
        try:
            # element = self.driver.find_element(*self.upgrade)
            element = WebDriverWait(self.driver, 12).until(lambda x: self.driver.base_find_element(*self.upgrade))
        except NoSuchElementException:
            self.logger.info("element is not find")
        except TimeoutException:
            self.logger.info(" find element timeout")
        else:
            self.logger.info("cancel upgrade")
            sleep(3)
            element.click()


if __name__ == '__main__':
    isupg = IsUpgrade()
    isupg.is_upgrade()
