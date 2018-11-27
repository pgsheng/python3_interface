"""
 从服务器推报警和日志到微信
 @Author  : pgsheng
 @Time    : 2018/11/27 14:41
 pip install apscheduler
"""
import os
import time

import requests
from apscheduler.schedulers.blocking import BlockingScheduler

from public.log import Log

"""
登入:用GitHub账号登入网站http://sc.ftqq.com/3.version，获得自己的SCKEY。
绑定:通过微信扫码关注完成绑定。
发消息:往 http://sc.ftqq.com/SCKEY.send 发GET请求，就可以在微信里收到消息。
"""


class ServerChan(object):

    def __init__(self):
        self.log = Log().get_logger()
        self.host = 'https://sc.ftqq.com/'
        self.sckey = 'SCU36505Te655df39dfe25061e9d9cbfa1a4faf925bfce30131860.send'

    def send(self):
        url = ''.join([self.host, self.sckey])
        # text：消息标题，最长为256，必填。
        # desp：消息内容，最长64Kb，可空，支持MarkDown。
        text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        params = {'text': text, 'desp': 'good'}
        r = requests.request('post', url=url, params=params) # get或post皆可
        if r.json()['errno'] == 0:
            self.log.info('发送成功')
        else:
            self.log.info('发送失败：%s' % r.json()['errmsg'])

    def timeing(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(func=self.send, trigger='cron', day_of_week='0-6',second='*/5')
        scheduler.start()


if __name__ == '__main__':
    ServerChan().send()
    # ServerChan().timeing()