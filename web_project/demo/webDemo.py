# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.com")
print(driver.title)
sleep(3)
driver.maximize_window()
sleep(2)
driver.refresh()
sleep(2)
driver.set_window_size(400,800)
sleep(2)
driver.back()
sleep(2)

driver.quit()
sleep(2)