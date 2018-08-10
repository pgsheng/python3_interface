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

# cd study_case
# locust -f locust_test.py --host=https://httpbin.org
# localhot:8089/
class UserBehavior(TaskSet):

	@task(1)
	def test_get(self):
		params = {'show_envs': '1'}
		with self.client.get("/get",params=params, catch_response=True) as response:
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
		r = self.client.post("/post",data=json)
		if r.status_code == 200:
			print(r.json())
			print("success---")
		else:
			print("fail----")


class WebsiteUser(HttpLocust):
	task_set = UserBehavior
	min_wait = 3000
	max_wait = 6000


