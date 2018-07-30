# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/6/3 17:33
'''
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from public import config
from public.log import Log


class BasePage(object):
	"""
		定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
	"""

	def __init__(self, url):
		self.log = Log().getLog()
		# 启动浏览器
		# driver = webdriver.Ie()
		# driver = webdriver.Edge()
		driver = webdriver.Firefox()
		# driver = webdriver.Chrome()
		driver.get(url)
		driver.maximize_window()
		driver.implicitly_wait(5)  # 隐式等待
		self.driver = driver

	def get_driver(self):
		return self.driver

	# 退出浏览器
	def quit(self):
		self.driver.quit()

	# 浏览器前进操作
	def forward(self):
		self.driver.forward()

	# 浏览器后退操作
	def back(self):
		self.driver.back()

	# 隐式等待
	def wait(self, seconds):
		self.driver.implicitly_wait(seconds)

	# 点击关闭当前窗口
	def close(self):
		try:
			self.driver.close()
		except NameError as e:
			self.log.error("Failed to quit the browser with %s" % e)

	# 保存图片
	def get_screenshot_img(self, name):
		now_time = time.strftime('%Y%m%d') + '_'
		screen_name = config.project_path + r'/test_screenshot/' + now_time + name + '.png'
		try:
			self.driver.get_screenshot_as_file(screen_name)
		except NameError as e:
			self.log.error("Failed to take screenshot! %s" % e)

	# 输入
	def send_keys(self, selector, text):
		el = self.find_element(selector)
		el.clear()
		try:
			el.send_keys(text)
		except NameError as e:
			self.log.error("Failed to type in input box with %s" % e)
			self.get_screenshot_img('send_keys_failure')

	# 清除文本框
	def clear(self, selector):
		el = self.find_element(selector)
		try:
			el.clear()
		except NameError as e:
			self.log.error("Failed to clear in input box with %s" % e)
			self.get_screenshot_img('clear_failure')

	# 点击元素
	def click(self, selector):
		el = self.find_element(selector)
		try:
			el.click()
		except NameError as e:
			self.log.error("Failed to click the element with %s" % e)
			self.get_screenshot_img('click_failure')

	# 或者网页标题
	def get_title(self):
		return self.driver.title

	@staticmethod
	def sleep(seconds):
		time.sleep(seconds)

	# 定位元素方法
	def find_element(self, selector):
		"""
		 这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
		 submit_btn = "id=>su"
		 login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
		 如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
		"""
		element = ''
		if '=>' not in selector:
			return self.driver.find_element_by_id(selector)
		selector_by = selector.split('=>')[0]
		selector_value = selector.split('=>')[1]

		if selector_by == "i" or selector_by == 'id':
			try:
				element = self.driver.find_element_by_id(selector_value)
			except NoSuchElementException as e:
				self.log.error("NoSuchElementException: %s" % e)
				self.get_screenshot_img("find_element_by_id_failure")  # take screenshot
		elif selector_by == "n" or selector_by == 'name':
			element = self.driver.find_element_by_name(selector_value)
		elif selector_by == "c" or selector_by == 'class_name':
			element = self.driver.find_element_by_class_name(selector_value)
		elif selector_by == "l" or selector_by == 'link_text':
			element = self.driver.find_element_by_link_text(selector_value)
		elif selector_by == "p" or selector_by == 'partial_link_text':
			element = self.driver.find_element_by_partial_link_text(selector_value)
		elif selector_by == "t" or selector_by == 'tag_name':
			element = self.driver.find_element_by_tag_name(selector_value)
		elif selector_by == "x" or selector_by == 'xpath':
			try:
				element = self.driver.find_element_by_xpath(selector_value)
			except NoSuchElementException as e:
				self.log.error("NoSuchElementException: %s" % e)
				self.get_screenshot_img("find_element_by_xpath_failure")
		elif selector_by == "s" or selector_by == 'selector_selector':
			element = self.driver.find_element_by_css_selector(selector_value)
		else:
			raise NameError("Please enter a valid type of targeting elements.")
		return element
