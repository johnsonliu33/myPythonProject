import unittest
from BeautifulReport import BeautifulReport
from time import sleep


class Testing2(unittest.TestCase):

    def test_case1(self):
        """ceshi1"""
        sleep(2)
        print("test1")
        self.assertTrue(True)

    def test_case2(self):
        """ceshi2"""
        print("test2")
        self.assertTrue(False)

    @unittest.skip("test_case3")
    def test_case3(self):
        """ceshi3"""
        print("test2")
        self.assertTrue(True)

    @BeautifulReport.add_test_img("error_img.png")
    def test_case4(self):
        """ceshi4"""
        print("test2")
        self.assertTrue(False)

    def test_case5(self):
        """ceshi5"""
        print("test2")
        self.assertTrue(True)