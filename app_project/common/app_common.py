from app_project.baseView.baseDriver import BaseDriver
from app_project.baseView.desired_caps import appium_desired
import time, os, csv
from app_project.common.app_log import my_log


class Common(BaseDriver):
    logger = my_log()

    @staticmethod
    def now_data():
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        return now

    # 截图
    def get_screen_shot(self, moudle):
        self.logger.info("get_screen_shot")
        times = self.now_data()
        image_file = os.path.dirname(os.path.dirname(__file__)) + "/screenShots/%s_%s.png" % (moudle, times)
        self.driver.get_screenshot_as_file(image_file)

    def get_window(self):
        x = self.get_win_size()["width"]
        y = self.get_win_size()["height"]
        z = (x, y)
        return z

    # 向上滑动
    def swipe_up(self):
        self.logger.info("swipe_up")
        s = self.get_window()
        x1 = int(s[0] * 0.5)
        y1 = int(s[1] * 0.8)
        y2 = int(s[1] * 0.2)
        self.swipes(x1, y1, x1, y2, 1000)

    # 获取参数
    def get_csv_data(file_name, line):
        with open(file_name, "r", encoding="utf-8-sig") as file:
            read = csv.reader(file)
            for row in enumerate(read, line):
                return row


if __name__ == "__main__":
    driver = appium_desired()
    c = Common(driver)
    c.is_upgrade()
    c.get_screen_shot("upgrade")
    c.swipe_up()
    csv_file = "../data/loginUser.csv"
    c.get_csv_data(csv_file, 3)
