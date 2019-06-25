# -*- cocoding:utf-8 -*-
import unittest
from time import sleep
import logging
import traceback
import ddt
from selenium.common.exceptions import NoSuchElementException
from web_project.src.common.myunit import StartEnd
from web_project.src.ddt_demo.data_mysql import DataBaseInfo

# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式：级别 时间 文件名[行号] 日志信息
    format="[%(levelname)s] %(asctime)s %(filename)s[line:%(lineno)d] %(message)s",
    # 打印日志的时间
    datefmt="%a, %Y-%m-%d %H:%M:%S",
    # 输出位置
    # 打开日志文件的方式
    filemode="w"
)


def get_data_from_mysql():
    db = DataBaseInfo(host="127.0.0.1",
                      port=3306,
                      db="test_data_db",
                      username="admin",
                      password="123456",
                      charset="utf8mb4")
    datas_tupl = db.get_data()
    db.close_conn()
    return datas_tupl


@ddt.ddt
class TestDemo(StartEnd):

    @ddt.data(*get_data_from_mysql())
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
