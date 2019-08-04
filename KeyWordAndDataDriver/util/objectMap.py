# -*- coding:utf-8 -*-

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from util.debugUtil import logger


# 获取单个页面元素对象
def getElement(driver, locationType, locatorExpression):
    try:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_element(by=locationType, value=locatorExpression))
        return element
    except NoSuchElementException:
        logger.error("Element %s not find" % locatorExpression)
    except TimeoutException:
        logger.error("Element %s find timeout" % locatorExpression)
    except Exception as e:
        logger.error(e)


# 获取多个页面元素对象，以list返回
def getElements(driver, locationType, locatorExpression):
    try:
        elements = WebDriverWait(driver, 3).until(lambda x: x.find_elements(by=locationType, value=locatorExpression))
        return elements
    except NoSuchElementException:
        logger.error("Element %s not find" % locatorExpression)
    except TimeoutException:
        logger.error("Element %s find timeout" % locatorExpression)
    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path="./../driver/geckodriver.exe")
    driver.get("http://www.baidu.com")
    searchBox = getElement(driver, "id", "kw")
    print(searchBox.tag_name)
    aList = getElements(driver, "tag name", "a")
    print(len(aList))
    driver.quit()
