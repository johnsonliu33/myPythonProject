import unittest, time
from BeautifulReport import BeautifulReport
from app_project.common.myUnittest import StartEnd
from multiprocessing import Process


def test_run():
    test_suit = unittest.defaultTestLoader.discover("../test_case", pattern="test*.py")
    result = BeautifulReport(test_suit)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="beatifulReportDemo", log_path="../report")


if __name__ == '__main__':
    # 构建进程组
    d_pocess = []
    d_list = ["62001", "62025"]
    # 加载进程
    for i in range(len(d_list)):
        devices = Process(target=test_run, args=(d_list[i],))
        d_pocess.append(devices)
    for dps in d_pocess:
        dps.start()
    for dps in d_pocess:
        dps.join()
