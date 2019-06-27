# -*- coding:utf-8 -*-
#
import unittest
from time import sleep
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from web_project.src.common.myunit import StartEnd
from web_project.src.util.web_log import my_log


@ddt.ddt
class TestDemo(StartEnd):
    def __init__(self):
        self.logs = my_log()

    @ddt.data(["神奇动物在哪里", "叶茨"], ["疯狂动物城", "古德温"], ["大话西游", "周星驰"])
    @ddt.unpack
    def test_dataDrivenByObj(self, testdata, expectdata):
        url = "http://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(8)
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException:
            self.logs.error("查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))
        except AssertionError:
            self.logs.info("搜索{}，期望{}，失败".format(testdata, expectdata))
        except Exception:
            self.logs.error("未知错误，错误信息：" + str(traceback.format_exc()))
        else:
            self.logs.info("搜索{}，期望{}，通过".format(testdata, expectdata))


if __name__ == '__main__':
    unittest.main()
