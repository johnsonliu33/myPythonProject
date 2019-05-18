import unittest, time
from BeautifulReport import BeautifulReport


def app_run():
    test_suit = unittest.defaultTestLoader.discover("src/test_case", pattern="testDemo*.py")
    result = BeautifulReport(test_suit)
    report_name = time.strftime("%Y_%m_%d %H_%M_%S") + "-report"
    result.report(filename=report_name, description="beatifulReportDemo", log_path="./report")


if __name__ == '__main__':
    app_run()
