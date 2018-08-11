# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : Alin
 @Time    : 2018/8/9 20:24
'''
import gevent
from gevent import monkey

gevent.monkey.patch_all()
import requests
from locust import HttpLocust, TaskSet, task

"""
   继承TaskSet类，为用户行为
   """

"""
@task() 装饰该方法为一个任务。1表示一个Locust实例被挑选执行的权重，数值越大，
执行频率越高
"""


class UserBehavior(TaskSet):

    @task(1)
    def test_get(self):
        params = {'show_envs': '1'}
        with self.client.get("/get", params=params, catch_response=True) as response:
            if response.status_code == 200:
                print(response.json())
                print("success---")
            else:
                print("fail----")

    @task(1)
    def test_post(self):
        json = {
            "info": {"code": 1, "sex": "男", "id": 1900, "name": "乔巴"},
            "code": 1,
            "name": "乔巴", "sex": "女",
            "id": 1990
        }
        r = self.client.post("/post", data=json)
        if r.status_code == 200:
            print(r.json())
            print("success---")
        else:
            print("fail----")


class WebsiteUser(HttpLocust):
    """
     设置性能测试
     """
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000


"""
# cd study_case

1、切换到性能测试脚本所在的目录，启动性能测试,控制台执行命令：
 locust -f test.py --host=https://httpbin.org
2、浏览器访问http://localhost:8089/
"""
