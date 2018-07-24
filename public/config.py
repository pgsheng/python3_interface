# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/4/7 15:22
'''
import os

base_url = 'https://httpbin.org/'  # 测试环境

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) # 获取本文件的上上级路径

# 上下关联接口参数可在这里定义变量存储
accessToken = ''
