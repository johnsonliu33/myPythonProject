# -*- coding:utf-8 -*-
import unittest
from HTMLTestRunner import BSTestRunner
from api.test_project.mysql_action import MysqlDB
import time
import yaml

# 初始化数据
db = MysqlDB()
f = open("datas.yaml", "r")
datas = yaml.full_load(f)
db.init_data(datas)

# 指定测试用例和测试报告路径
case_dir = "."
report_dir = "./report"
# 加载测试用例
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*.py")
# 定义报告的文件格式
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + "/" + now + " report.html"
# 运行用例并生成测试报告
with open(report_name, "wb")as file:
    runner = BSTestRunner.BSTestRunner(stream=file,verbosity=2, title="api_report", description="api test report")
    runner.run(discover)
