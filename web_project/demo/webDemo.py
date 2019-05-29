# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

# driver=webdriver.Firefox()
# driver=webdriver.Chrome()
driver=webdriver.Ie()
driver.implicitly_wait(8)
driver.get("http://www.baidu.com")
print(driver.title)
sleep(3)
driver.maximize_window()
sleep(3)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.refresh()
sleep(3)
driver.set_window_size(400, 800)
sleep(3)
driver.back()



driver.quit()
