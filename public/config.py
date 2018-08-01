# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/7 15:22
"""
import os

# 主机
base_url = 'https://httpbin.org/'
# 获取本文件的上上级路径（这里是获取项目路径）
project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

test_case_path = project_path + '//test_case//'
test_data_path = project_path + '//test_data//'
test_report_path = project_path + '//test_report//'
test_log_path = project_path + '//test_log//'
test_screenshot_path = project_path + '//test_screenshot//'
sdk_path = project_path + '//sdk//'

# 上下关联接口参数可在这里定义变量存储
accessToken = ''
