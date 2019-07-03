# -*- coding:utf-8 -*-
from lettuce import world, step
from selenium import webdriver
import time


@step('将搜索词设定为书的名字"(,*)"')
def have_bsidu_website(step, searchWord):
    world.searchWord = searchWord
    print(world.searchWord)


@step('打开百度网站')
def visit_baidu_website(step):
    world.driver = webdriver.Firefox(executable_path="D:\myPythonProject\web_project\driver\geckodriver.exe")
    world.driver.get("http://www.baidu.com")


@step('在搜索输入框输入搜索的关键词，并单机搜索按钮后')
def search_in_sougou_website(step):
    world.driver.find_element_by_id("kw").send_keys(world.searchWord)
    world.driver.find_element_by_id("su").click()
    time.sleep()


@step('在搜索结果中可以看到书的作者"(.*)"')
def check_result_in_sougou(step, searchResult):
    assert searchResult in world.driver.page_source, "not got words:%s" % searchResult
    world.driver.quit()
