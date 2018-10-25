# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/25 15:23
"""
import redis as redis

from public.log import Log


class RedisStudy(object):

    def __init__(self):
        self.log = Log().get_logger()

    def study(self):
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        r.set('name', 'zhangsan')  # 添加
        self.log.info(r.get('name'))  # 获取

if __name__ == '__main__':
    r = RedisStudy()
    r.study()

"""
启动服务：
redis-server.exe C:\AToolSofrware\Redis\redis.windows.conf 
查看是否成功：
redis-cli
"""