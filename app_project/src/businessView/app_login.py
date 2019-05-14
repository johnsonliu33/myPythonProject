from time import sleep

from app_project.src.common.app_common import Common
from selenium.webdriver.common.by import By

from app_project.src.baseView.desired_caps import devices_start
from app_project.src.util.app_log import my_log


class LoginView(Common):
    logger = my_log()
    username_type = (By.ID, "com.jiandan.mobilelesson:id/account_et")
    password_type = (By.ID, "com.jiandan.mobilelesson:id/password_et")
    login_btn = (By.ID, "com.jiandan.mobilelesson:id/login_btn")

    def login_action(self, username, password):
        self.is_upgrade()
        self.get_screen_shot("login")

        self.logger.info("login username: %s" % username)
        self.driver.base_find_element(*self.username_type).send_keys(username)
        self.logger.info("login password: %s" % password)
        self.driver.base_find_element(*self.password_type).send_keys(password)
        self.driver.base_find_element(*self.login_btn).click()
        sleep(5)
        self.swipe_up()


if __name__ == "__main__":
    driver = devices_start()
    on = LoginView(driver)
    on.login_action("jianeryou1", "abc123")
