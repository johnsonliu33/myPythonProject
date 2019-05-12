# -*- coding:utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class IsUpgrade:
    def __init__(self, driver):
        self.driver = driver
        self.upgrade = (By.ID, "com.guideclasspad:id/cancel_tv")

    # 取消升级
    def is_upgrade(self):
        self.logger.info("is_upgrade")
        try:
            # element = self.driver.find_element(*self.upgrade)
            element = WebDriverWait(self.driver, 12).until(lambda x: self.driver.find_element(*self.upgrade))
        except NoSuchElementException:
            self.logger.info("element is not find")
        except TimeoutException:
            self.logger.info(" find element timeout")
        else:
            self.logger.info("cancel upgrade")
            sleep(3)
            element.click()
