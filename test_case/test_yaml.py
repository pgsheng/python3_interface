# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
'''
import yaml
from public import Config

def read_yaml():
	# 你的yaml格式文件路径
	path = Config.project_path + r'\test_data\yaml_test_data.yaml'

	with open(path,'r',encoding='utf-8') as file:
		# 将yaml格式内容转换成 dict类型
		# yaml_data = yaml.load(file)
		load_data = yaml.load(file.read())
		print(load_data)
		print(load_data.get('complex'))

	with open(path, 'r', encoding='utf-8') as file:
		# load_all返回的是一个迭代器对象，需要自己去遍历获取每一个段的转换后才python对象。
		load_all_data = yaml.load_all(file.read())
		# 遍历迭代器
		for data in load_all_data:
			print(data)
			print(data.get('complex'))

def write_yaml():
	# 你的yaml格式文件路径
	path = Config.project_path + r'\test_data\yaml_test_data.yaml'
	# 待写入的数据
	data = {'complex2': {'languages': ['Ruby', 'Perl', 'Python'], 'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org'}}}

	# a追加写入，w覆盖写入
	with open(path,'a',encoding='utf-8') as file:
		# 将python对象转换成为yaml格式文档
		yaml.dump(data, file)

def read_txt():
	# 你的yaml格式文件路径
	path = Config.project_path + r'\test_data\aa.txt'

	# a追加写入，w覆盖写入
	with open(path,'r',encoding='utf-8') as file:
		# 将python对象转换成为yaml格式文档
		# data = file.read()
		data = file.readline()
		print(data)

if __name__ == '__main__':
	# read_yaml()
	# write_yaml()
	read_txt()