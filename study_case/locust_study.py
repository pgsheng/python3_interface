# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : Alin
 @Time    : 2018/8/9 20:24
'''
import os

import gevent
from gevent import monkey

gevent.monkey.patch_all()
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    """
       继承TaskSet类，为用户行为
    """

    @task(1)
    def test_get(self):
        params = {'show_envs': '1'}
        with self.client.get("/get", params=params, catch_response=True) as response:
            if response.status_code == 200:
                print(response.json())
                response.success()
            else:
                print("fail----")

    """
    @task() 装饰该方法为一个任务。1表示一个Locust实例被挑选执行的权重，数值越大，
    执行频率越高
    """

    @task(1)
    def test_post(self):
        json = {
            "info": {"code": 1, "sex": "男", "id": 1900, "name": "乔巴"},
            "code": 1,
            "name": "乔巴", "sex": "女",
            "id": 1990
        }
        r = self.client.post("/post", data=json, catch_response=True)
        if r.status_code == 200:
            print(r.json())
            r.success()
        else:
            r.failure("fail----")  # 失败断言


class WebsiteUser(HttpLocust):
    """
     设置性能测试
    """
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    host = 'https://httpbin.org' # 指定压测地址

"""
# cd study_case
  
1、切换到性能测试脚本所在的目录，启动性能测试,控制台执行命令：
 locust -f locust_study.py 
2、浏览器访问http://localhost:8089/
"""


if __name__ == '__main__':
    # os.system('locust -f locust_study.py')
    os.system('locust -f locust_study.py  --no-web -c 80 -r 10 --csv=测试 --logfile=a.log')

"""
-f ：指定性能测试脚本文件
--host ：指定压测地址 如,--host=https://httpbin.org
--port ：指定端口 如,--port=8089
--no-web ：表示不使用web界面运行测试
-c ：设置虚拟用户数
-r ：设置每秒启动虚拟用户数
-t : 设置运行时间
--only-summary ：只打印摘要统计
--csv=CSVFILEBA：以CSV格式存储当前请求测试数据，--csv=测试
----logfile=LOGFILE ：日志文件路径，--logfile=a.log
"""