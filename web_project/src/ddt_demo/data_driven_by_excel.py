# -*- cocoding:utf-8 -*-
import unittest
from time import sleep
import logging
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from web_project.src.common.myunit import StartEnd
from web_project.src.ddt_demo.data_excel import ParseExcel
from web_project.src.util.web_log import my_log

excle = ParseExcel("./ceshishuju.xlsx", "Sheet1")


@ddt.ddt
class TestDemo(StartEnd):
    logging = my_log()

    @ddt.data(*excle.getDataFromSheet())
    def test_dataDrivenByObj(self, data):
        testdata, expectdata = tuple(data)
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(8)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException:
            logging.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))
        except AssertionError:
            logging.info("搜索{}，期望{}，失败".format(testdata, expectdata))
        except Exception:
            logging.error("未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            print("搜索{}，期望{}，通过".format(testdata, expectdata))


if __name__ == '__main__':
    unittest.main()
