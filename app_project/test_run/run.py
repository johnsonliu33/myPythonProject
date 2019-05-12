import unittest, time
from BeautifulReport import BeautifulReport


def test_run():
    test_suit = unittest.defaultTestLoader.discover("../test_case", pattern="test*.py")
    result = BeautifulReport(test_suit)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="beatifulReportDemo", log_path="../report")


if __name__ == '__main__':
    test_run()
