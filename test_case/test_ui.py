# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
'''
import time
import unittest

import yaml
from ddt import ddt, data
from selenium import webdriver

from public import base, config
from public.log import Log

testdata = base.get_excel_data('test.xlsx', 'test2')


@ddt
class BaiduSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.log = Log('ui测试').getLog()

        file_path = config.project_path + r'\test_data\html_element_data.yaml'
        with open(file_path, 'r', encoding='utf-8') as file:
            # 将yaml格式内容转换成 dict类型
            self.loaddata = yaml.load(file)

        self.driver = webdriver.Ie()
        # self.driver = webdriver.Chrome()  # 获取浏览器驱动对象
        # self.driver = webdriver.Firefox()  # 获取浏览器驱动对象
        self.driver.get(self.loaddata.get('baidu').get('url'))  # 打开百度网页

    @data(*testdata)
    def test_something(self, data):
        u'''测试用例'''
        try:
            self.driver.find_element_by_xpath(self.loaddata.get('baidu').get('input')).clear()
            self.driver.find_element_by_xpath(self.loaddata.get('baidu').get('input')).send_keys(
                data.get("name"))
            time.sleep(1)
            self.driver.find_element_by_xpath(self.loaddata.get('baidu').get('search')).click()

            time.sleep(1)
            self.driver.get_screenshot_as_file(
                config.project_path + r'\test_screenshot\%s.png' % data.get("id"))

            time.sleep(1)
            self.log.info("检查点->：" + self.driver.title)
            self.assertEqual(self.driver.title, 'sheng_百度搜索', msg='和预期不一样')
        except Exception as e:
            self.log.error("执行用例失败-> %s" % e)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        # pass


if __name__ == '__main__':
    unittest.main()
