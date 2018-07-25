# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/7 15:22
'''
import os

# 主机
base_url = 'https://httpbin.org/'

# 获取本文件的上上级路径（这里是获取项目路径）
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

# 上下关联接口参数可在这里定义变量存储
accessToken = ''
