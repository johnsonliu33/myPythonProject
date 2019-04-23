import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suit = unittest.defaultTestLoader.discover("../testCase", pattern="testReport.py")
    result = BeautifulReport(test_suit)
    name=time.strftime("%Y_%m_%d %H_%M")+"_report"
    result.report(filename=name, description="定制名师课", log_path="../report")
