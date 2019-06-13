from django.test import TestCase
import requests
import unittest


# Create your tests here.

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/users/"
        self.auth = ("root", "123456")

    def test_get_user(self):
        resp = requests.get(url=self.base_url + "1/", auth=self.auth)
        result = resp.json()
        print(result)
        self.assertEqual(result["username"], "root")
        self.assertEqual(result["email"], "779446928@qq.com")

    def test_add_user(self):
        from_data = {"username": "xiaoming4", "email": "123@qq.com"}
        resp = requests.post(url=self.base_url, data=from_data, auth=self.auth)
        result = resp.json()
        print(result)
        self.assertEqual(result["username"], "xiaoming4")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
