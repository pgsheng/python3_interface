# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
'''
import unittest


from public import base
from ddt import ddt,data

from public.log import Log

testdata = base.get_excel_data('test.xlsx', 'test')

@ddt
class MyTestCase(unittest.TestCase):
	u'''测试'''

	@classmethod
	def setUpClass(self):
		self.log = Log('测试').getLog()

	@data(*testdata)
	def test_something(self,data):
		u'''测试用例'''

		r = base.get_excel_response(data)
		base.write_to_excel('test.xlsx', 'test', data, r)

		self.log.info("检查点->：" + data.get('checkpoint'))
		self.log.info("实际返回结果->：" + r.text)
		if data.get('isCheckStatusCode'):
			self.assertEqual(str(r.status_code), data.get('checkpoint'),msg='和预期不一样')
		else:
			self.assertTrue(data.get('checkpoint') in r.text,msg='和预期不一样')

	@classmethod
	def tearDownClass(self):
		pass


if __name__ == '__main__':
	unittest.main()
