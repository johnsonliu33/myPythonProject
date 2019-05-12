from app_project.common.app_common import Common
from selenium.webdriver.common.by import By
from app_project.baseView.desired_caps import appium_desired
from time import sleep
from app_project.common.app_log import my_log


class LoginView(Common):
    logger=my_log()
    username_type = (By.ID, "com.jiandan.mobilelesson:id/account_et")
    password_type = (By.ID, "com.jiandan.mobilelesson:id/password_et")
    login_btn = (By.ID, "com.jiandan.mobilelesson:id/login_btn")

    def login_action(self, username, password):
        self.is_upgrade()
        self.get_screen_shot("login")

        self.logger.info("login username: %s" % username)
        self.driver.find_element(*self.username_type).send_keys(username)
        self.logger.info("login password: %s" % password)
        self.driver.find_element(*self.password_type).send_keys(password)
        self.driver.find_element(*self.login_btn).click()
        sleep(5)
        self.swipe_up()


if __name__ == "__main__":
    driver = appium_desired()
    on = LoginView(driver)
    on.login_action("jianeryou1", "abc123")
