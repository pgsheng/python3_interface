"""
 @Author  : pgsheng
 @Time    : 2018/6/7 16:44
"""

import unittest

from public import base
from public.log import Log

from urllib import request
from http import cookiejar


class TestCookie(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = Log("cookie测试").get_logger()
        cls.url = base.get_url("cookies/set")
        pass

    def test_cookie1(self):
        cookie = {"freeform": "me"}
        r = base.get_response("get", self.url, cookies=cookie)
        self.log.info(r.text)

    def test_cookie2(self):
        # 声明一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler = request.HTTPCookieProcessor(cookie)
        # 通过CookieHandler创建opener
        opener = request.build_opener(handler)
        # 此处的open方法打开网页
        response = opener.open('http://www.baidu.com')
        # 打印cookie信息
        for item in cookie:
            self.log.info('name = %s' % item.name)
            self.log.info('Value = %s' % item.value)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
