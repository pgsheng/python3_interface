# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
'''
import time
import unittest

import yaml
from selenium import webdriver

from public import base, config
from ddt import ddt,data

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
			self.load_data = yaml.load(file)

		self.dirvier = webdriver.Firefox()  # 获取浏览器驱动对象
		self.dirvier.get(self.load_data.get('baidu').get('url'))  # 打开百度网页

	@data(*testdata)
	def test_something(self,data):
		u'''测试用例'''

		self.dirvier.find_element_by_xpath(self.load_data.get('baidu').get('input')).send_keys(data.get("name"))
		self.dirvier.find_element_by_xpath(self.load_data.get('baidu').get('search')).click()
		time.sleep(3)
		self.log.info("检查点->：" + self.dirvier.title)
		self.assertEqual(self.dirvier.title, 'pgsheng_百度搜索',msg='和预期不一样')

	@classmethod
	def tearDownClass(self):
		self.dirvier.quit()
		# pass

if __name__ == '__main__':
	unittest.main()
