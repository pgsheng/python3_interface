# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
"""
import csv
import json
import os
import yaml
from public import config


def read_yaml():
    # 你的yaml格式文件路径
    # path = config.project_path + r'\study_case\data\yaml_study_data.yaml'
    path = os.path.join(config.study_case_path,'data','yaml_study_data.yaml')

    with open(path, 'r', encoding='utf-8') as file:
        # 将yaml格式内容转换成 dict类型
        load_data = yaml.load(file)
        # load_data = yaml.load(file.read())
        print(load_data)
        # print(load_data.get('complex'))

    # with open(path, 'r', encoding='utf-8') as file:
    #     # load_all返回的是一个迭代器对象，需要自己去遍历获取每一个段的转换后才python对象。
    #     load_all_data = yaml.load_all(file.read())
    #     # 遍历迭代器
    #     for data in load_all_data:
    #         print(data)
    #         print(data.get('complex'))


def write_yaml():
    # 你的yaml格式文件路径
    path = config.project_path + r'\study_case\data\yaml_study_data.yaml'
    # 待写入的数据
    data = {'complex2': {'languages': ['Ruby', 'Perl', 'Python'],
                         'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org'}}}

    # a追加写入，w覆盖写入
    with open(path, 'a', encoding='utf-8') as file:
        # 将python对象转换成为yaml格式文档
        yaml.dump(data, file)


"""
txt文件读写测试
"""


def read_txt():
    # 文件路径
    path = config.project_path + r'\study_case\data\aa.txt'

    with open(path, 'r', encoding='utf-8') as file:
        data = file.read()
        # data = file.readline()
        print(data)


def read_json():
    path = os.path.join(config.study_case_path,'data','sina7x24.json')

    with open(path, 'r', encoding='utf-8') as file:
        load_data = json.load(file) # 文件流对象
        print(load_data)

    with open(path, 'r', encoding='utf-8') as file:
        load_all_data = json.loads(file.read()) # 字符串
        for data in load_all_data:
            print(data)

    with open(path, 'r', encoding='utf-8') as file:
        load_all_data = file.read()
        print(load_all_data) # 字符串 str


def write_json():
    path = os.path.join(config.study_case_path,'data','sina7x24.json')
    data = {'complex2': {'languages': ['Ruby', 'Perl', 'Python'],
                         'websites': {'YAML': 'yaml.org', 'Ruby': 'ruby-lang.org', 'Python': 'python.org'}}}
    # a追加写入，w覆盖写入
    with open(path, 'w', encoding='utf-8') as file:
        # 将python对象转换成为yaml格式文档
        json.dump(data, file)

def read_csv():
    path = os.path.join(config.study_case_path,'data','teachers.csv')


    with open(path, 'r', newline='') as file:
        load_data = csv.reader(file) # 文件流对象
        for data in load_data:
            print(data)

    return load_data


def write_csv():
    path = os.path.join(config.study_case_path,'data','teachers1.csv')
    # a追加写入，w覆盖写入
    with open(path, 'a', encoding='utf-8',newline='') as file:
    # file = open(path, 'a', newline='')
        csv_write = csv.writer(file, dialect='excel')
        csv_items = [['郭老师', '高级讲师', '及入侵分析。']]
        for item in csv_items:
            csv_write.writerow(item)

if __name__ == '__main__':
    read_yaml()
# write_yaml()
#     read_txt()
#     read_json()
#     write_json()
#     read_csv()
#     write_csv()