# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : Alin
 @Time    : 2018/6/3 17:33
'''
from selenium import webdriver

from public.log import Log


def test_webdriver():
	log = Log("UI测试").getLog()

	dirvier = webdriver.Firefox() # 获取浏览器驱动对象

	dirvier.get('https://www.baidu.com/') # 打开一个网页
	# dirvier.find_element_by_id('kw').clear() # 清除文本
	'''HTMl的属性定位,属性要唯一才能定位到'''
	# dirvier.find_element_by_id('kw').send_keys('王春玲') # 根据html属性id定位元素，模拟按键输入
	# dirvier.find_element_by_name('wd').send_keys('王春玲') # 根据html属性name定位元素，模拟按键输入
	# dirvier.find_element_by_class_name('s_ipt').send_keys('王春玲') # 根据html属性id定位元素，模拟按键输入
	# dirvier.find_element_by_tag_name('input').send_keys('王春玲') # 根据标签input定位，这里定位不到，因为页面有多个input
	# dirvier.find_element_by_link_text('贴吧').click() # 根据标签对之间的文本信息定位，如：<a>贴吧</a>
	# dirvier.find_element_by_partial_link_text('一个很长').click() # 根据标签对之间的部分文本信息定位，如：<a>一个很长很长的文本</a>
	'''XPath定位'''
	# dirvier.find_element_by_xpath('/html/body/div/div/div[4]/div/div/from/span/input').send_keys('王春玲') # ，绝对路径定位
	# dirvier.find_element_by_xpath('//input[@id="kw"]').send_keys('王春玲') # XPath定位，根据元素属性id,还可以其他属性，//表示当前页面某目录
	# dirvier.find_element_by_xpath('//*[@id="kw"]').send_keys('王春玲') # XPath定位，根据元素属性，不指定标签名，用*替代
	# dirvier.find_element_by_xpath("//form[@id='form']/span/input").send_keys('王春玲') # XPath定位，上级和属性组合，
	# dirvier.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]').send_keys('王春玲') # 多个属性组合
	'''CSS定位,属性要唯一才能定位到'''
	# dirvier.find_element_by_css_selector(".s_ipt").send_keys('王春玲') # css的class属性，注意：.代表class类型的
	# dirvier.find_element_by_css_selector("#kw").send_keys('王春玲') # css的id属性，注意：#代表id类型的
	# dirvier.find_element_by_css_selector("input").send_keys('王春玲') # 标签名定位，这里定位不到，不唯一
	dirvier.find_element_by_css_selector("span>input").send_keys('王春玲') # 父子关系



	# dirvier.find_element_by_id('kw').submit() # 提交输入框的内容,功能与click类似
	# dirvier.find_element_by_id('su').click() # 点击元素
	dirvier.find_element_by_xpath('//*[@id="su"]').click() # 点击元素
	# size = dirvier.find_element_by_id('kw').size # 获取元素的大小
	# text = dirvier.find_element_by_id('cp').text # 获取元素的文本
	# attribute = dirvier.find_element_by_id('kw').get_attribute() # 获取元素的属性值
	# print(size)


	# dirvier.get_screenshot_as_file(Config.project_path + r'\test_data\a.png') # 截屏

	# time.sleep(3) #睡眠3秒
	# dirvier.back() # 返回上一个网页
	# time.sleep(3)
	# dirvier.refresh() # 刷新当前页面
	# dirvier.forward() # 前进

	# dirvier.set_window_size(540,960) # 设置窗口大小
	# dirvier.maximize_window() # 设置窗口最大化
	# dirvier.minimize_window() # 设置窗口最小化

	log.info(dirvier.title) # 获取标题

	dirvier.quit()
	# dirvier.close()

if __name__ == '__main__':
	test_webdriver()