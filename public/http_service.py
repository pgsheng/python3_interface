# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/3/31 22:29
"""

import requests

from public.log import Log


class MyHTTP(object):
    """网络请求封装"""

    def __init__(self):
        self.log = Log('MyHTTP').get_logger()

    def get(self, url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        cookies = kwargs.get('cookies')
        try:
            r = requests.get(url, params=params, headers=headers, cookies=cookies, timeout=15)
            return r
        except Exception as e:
            self.log.error('get请求出错:%s' % e)

    def put(self, url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        data = kwargs.get('data')
        json = kwargs.get('json')
        cookies = kwargs.get('cookies')
        try:
            r = requests.put(url, params=params, headers=headers, data=data, json=json, cookies=cookies, timeout=30)
            return r
        except Exception as e:
            self.log.error("put请求出错:%s" % e)

    def post(self, url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        data = kwargs.get('data')
        json = kwargs.get('json')
        cookies = kwargs.get('cookies')
        try:
            r = requests.post(url, params=params, headers=headers, data=data, json=json, cookies=cookies, timeout=100)
            return r
        except Exception as e:
            self.log.error('post请求出错:%s' % e)

    def delete(self, url, **kwargs):
        params = kwargs.get('params')
        headers = kwargs.get('headers')
        data = kwargs.get('data')
        json = kwargs.get('json')
        cookies = kwargs.get('cookies')
        try:
            r = requests.delete(url, params=params, headers=headers, data=data, json=json, cookies=cookies, timeout=15)
            return r
        except Exception as e:
            self.log.error('detele请求出错:%s' % e)
