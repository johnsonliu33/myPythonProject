import unittest
import time
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suit = unittest.defaultTestLoader.discover("../testCase", pattern="caseDemo*.py")
    result = BeautifulReport(test_suit)
    name=time.strftime("%Y_%m_%d %H_%M_%S")+"-report"
    result.report(filename=name, description="beatifulReportDemo", log_path="../report")
