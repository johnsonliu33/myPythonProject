import unittest
from BeautifulReport import BeautifulReport

class Testing(unittest.TestCase):

    def test_case1(self):
        """ceshi"""
        print("test1")
        self.assertTrue(True)

    def test_case2(self):
        print("test2")
        self.assertTrue(True)

    @unittest.skip("test_case3")
    def test_case3(self):
        print("test2")
        self.assertTrue(True)

    @BeautifulReport.add_test_img('../img/错误截图.png')
    def test_case4(self):
        print("test2")
        self.assertTrue(False)

    def test_case5(self):
        print("test2")
        self.assertTrue(True)
