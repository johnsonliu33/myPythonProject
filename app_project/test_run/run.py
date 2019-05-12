import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suit = unittest.defaultTestLoader.discover("../test_case", pattern="test*.py")
    result = BeautifulReport(test_suit)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="beatifulReportDemo", log_path="../report")
