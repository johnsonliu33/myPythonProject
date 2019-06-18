# -*- coding:utf-8 -*-
from locust import TaskSet, HttpLocust, task


class UserBehavior(TaskSet):
    def on_start(self):
        # 设置user和group参数下标参数值
        self.users_index = 0
        self.groups_index = 0

    @task(2)  # 请求比例2:1
    def test_users(self):
        #读取参数
        users_id=self.locust.id[self.users_index]
        url="/users/"+str(users_id)+"/"
        self.client.get(url, auth=("admin", "123456"))
        #取余运算循环遍历参数
        self.users_index=(self.users_index+1)%len(self.locust.id)
    @task(1)  # 请求比例1:1
    def test_groups(self):
        groups_id=self.locust.id[self.groups_index]
        url="/groups/"+str(groups_id)+"/"
        self.client.get("/groups/", auth=("admin", "123456"))
        self.groups_index=(self.groups_index+1)%len(self.locust.id)

class WebsitUser(HttpLocust):
    task_set = UserBehavior
    #参数配置
    id=[1,2]
    min_wait = 3000
    max_wait = 6000
    host = "http://127.0.0.1:8000"
# 运行：locust -f D:\..\*_api_locust.py --host=127.0.0.1:8000
# Number of users to simulate:设置模拟用户数
# Hatch rate (users spawned/second):每秒启动的虚拟用户数
