# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.title)
sleep(3)
driver.maximize_window()
driver.refresh()
driver.set_window_size(400, 800)
driver.back()

# 获取元素 8个
driver.find_elements_by_id()
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_elements_by_xpath()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
driver.find_element_by_tag_name()
driver.find_element_by_css_selector()

driver.quit()
