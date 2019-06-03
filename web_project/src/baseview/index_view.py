# -*- coding:utf-8 -*-
from web_project.src.basepage.base_page import BasePage
from selenium.webdriver.common.by import By


class IndexView(BasePage):
    api = "/index.php"
    # 定位器
    zentao_type = (By.ID, "zentaopro")

    def type_zentao(self):
        self.find_element(*self.zentao_type).click()

    def test_zt_type(driver):
        viewindex=IndexView(driver)
        viewindex.open(viewindex.api)
        viewindex.type_zentao()
