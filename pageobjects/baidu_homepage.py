# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/6/3 17:33
'''
from public.base_page import BasePage


class HomePage(BasePage):

	def __init__(self):
		self.input_box = "id=>kw"
		self.search_submit_btn = "xpath=>//*[@id='su']"
		self.news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"	# 百度新闻入口

		super(HomePage, self).__init__("https://www.baidu.com/")

	def search_input(self, text):
		self.send_keys(self.input_box, text)

	def send_submit_btn(self):
		self.click(self.search_submit_btn)

	def click_news(self):
		self.click(self.news_link)
		self.sleep(2)
