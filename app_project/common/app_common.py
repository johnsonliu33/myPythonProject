from app_project.baseView.baseDriver import BaseDriver
from app_project.baseView.desired_caps import appium_desired
import logging.config
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import csv

CON_LOG = "../config/log.conf"
logging.config.fileConfig(CON_LOG)
logs = logging.getLogger()


class Common(BaseDriver):
    upgrade = (By.ID, "com.guideclasspad:id/cancel_tv")

    def is_upgrade(self):
        logs.info("is_upgrade")
        try:
            # element = self.driver.find_element(*self.upgrade)
            element = WebDriverWait(self.driver, 12).until(lambda x: self.driver.find_element(*self.upgrade))
        except NoSuchElementException:
            logs.info("element is not find")
        except TimeoutException:
            logs.info(" find element timeout")
        else:
            logs.info("cancel upgrade")
            time.sleep(3)
            element.click()

    def getTimes(self):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        return now

    def get_screen_shot(self, moudle):
        logs.info("get_screen_shot")
        times = self.getTimes()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenShots/%s_%s.png" % (moudle, times)
        self.driver.get_screenshot_as_file(image_file)

    def get_window(self):
        x = self.get_win_size()["width"]
        y = self.get_win_size()["height"]
        return (x, y)

    def swipe_up(self):
        logs.info("swipe_up")
        s = self.get_window()
        x1 = int(s[0] * 0.5)
        y1 = int(s[1] * 0.8)
        y2 = int(s[1] * 0.2)
        self.swipes(x1, y1, x1, y2, 1000)

    def get_csv_data(file_name, line):
        with open(file_name, 'r', encoding='utf-8-sig')as file:
            read = csv.reader(file)
            for index, row in enumerate(read, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    c = Common(driver)
    c.is_upgrade()
    c.get_screen_shot("upgrade")
    c.swipe_up()
