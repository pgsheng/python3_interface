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
        # 1、一般连接方式
        r = redis.Redis(host='127.0.0.1', port=6379, db=0, password=12345)
        # r.set('name', 'zhangsan0')  # 添加
        self.log.info(r.get('mykey1'))  # 获取

        # 2、连接池
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, password=12345)
        r = redis.Redis(connection_pool=pool)
        # r.set('name2', 'zhangsan2')  # 添加
        # r.setex('name2', 'zhangsan11',15)  #设置过期时间（秒）
        self.log.info(r.get('name2'))  # 获取

        # r.mset(name3='zhangsan', name4='lisi')    # 批量设置值
        self.log.info(r.mget("name3", "name4"))
        self.log.info(r.mget(["name3", "name4"]))

        self.log.info(r.getset("name2", "wangwu"))  #  设置新值，打印原值
        self.log.info(r.get("name2"))  # 输出新值
        self.log.info(r.getrange("name2", 0, 3))  # #根据字节获取子序列

if __name__ == '__main__':
    r = RedisStudy()
    r.study()

"""
启动服务： redis-server.exe C:\AToolSofrware\Redis\redis.windows.conf 
查看是否成功： redis-cli
输入密码验证才能使用：auth 12345
关闭：redis-cli -a 12345 shutdown (没有密码不要-a)
"""
