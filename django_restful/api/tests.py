from django.test import TestCase
import requests
import unittest


# Create your tests here.

class TestUser(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/users"
        self.auth = ("admin", "123456")

    def test_get_user(self):
        resp = requests.get(url=self.base_url + "/1/", auth=self.auth)
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

    def test_delete_user(self):
        self.assertEqual()

    def test_update_user(self):
        self.assertEqual()

    def test_auth_no(self):
        self.assertEqual()

    def tearDown(self):
        pass


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/groups"
        self.auth = ("admin", "123456")

    def test_get_group(self):
        resp = requests.get(url=self.base_url + "/1/", auth=self.auth)
        result = resp.json()
        print(result)
        self.assertEqual(result["name"], "group1")

    def test_add_group(self):
        from_data = {"name": "xiaoming4"}
        resp = requests.post(url=self.base_url, data=from_data, auth=self.auth)
        result = resp.json()
        print(result)
        self.assertEqual(result["name"], "xiaoming4")

    def test_delete_group(self):
        self.assertEqual()

    def test_update_group(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
