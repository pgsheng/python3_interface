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
    # read_yaml()
# write_yaml()
#     read_txt()
#     read_json()
#     write_json()
#     read_csv()
#     write_csv()
    load_all_data = json.loads("""{
	"list": [{"app_msg_ext_info": {
			"audio_fileid": 0,
			"author": "",
			"content": "",
			"content_url": "/s?timestamp=1544172713&amp;src=3&amp;ver=1&amp;signature=Gre6njwniYx0L1O1iEHLrUVnpbHyAh8nGsdm8F*0ypJTTqy0rWpOdEMheDl8vpMyGPt3Svd9-c6Baty-rd7l6BWm0SKuGiReBHsq224F6E6-VPe60wLraXTpGOMRzS-QdDH*s8z0*I-JsfeDD6Px4mN6n3nam4LmILZu9lPVtY4=",
			"copyright_stat": 100,
			"cover": "http://mmbiz.qpic.cn/mmbiz_jpg/yD1rHictxt27sdiarpoDrp47icCRMhfww6z9zzrMsHuF7BtEGqtJLgkgTCqZ6ImvEjVGXicSIWbYlgmYRhIPZuqVUw/0?wx_fmt=jpeg",
			"del_flag": 1,
			"digest": "“好想养只犬系小男友啊！”最近总能听到这样的感叹。大部分女生都对犬系男抱有深深的迷之向往。（图源：@yuk1",
			"duration": 0,
			"fileid": 503054819,
			"is_multi": 1,
			"item_show_type": 0,
			"malicious_content_type": 0,
			"malicious_title_reason_id": 0,
			"multi_app_msg_item_list": [{
				"audio_fileid": 0,
				"author": "",
				"content": "",
				"content_url": "/s?timestamp=1544172713&amp;src=3&amp;ver=1&amp;signature=Gre6njwniYx0L1O1iEHLrUVnpbHyAh8nGsdm8F*0ypJTTqy0rWpOdEMheDl8vpMyGPt3Svd9-c6Baty-rd7l6BWm0SKuGiReBHsq224F6E4zdute3IJlToLIQ1IW3h-XSDkIjZNqu29EzyOvKK0zbhDujR6C2E*qApSD2xe7fN8=",
				"copyright_stat": 100,
				"cover": "http://mmbiz.qpic.cn/mmbiz_jpg/yD1rHictxt27sdiarpoDrp47icCRMhfww6z5hMbmYAPxxVicgdyvWkWFeGjGQ1Yz8xWUnG9EgibcTGUn6xac7y7zG3g/0?wx_fmt=jpeg",
				"del_flag": 1,
				"digest": "1羊台山森林公园羊台山森林公园位于深圳市西北部，为深圳八景之一，主峰海拔581.7米，为深圳市西部的最高点。",
				"duration": 0,
				"fileid": 503054817,
				"item_show_type": 0,
				"malicious_content_type": 0,
				"malicious_title_reason_id": 0,
				"play_url": "",
				"source_url": "",
				"title": "深圳那些隐藏的美景"
			}],
			"play_url": "",
			"source_url": "",
			"subtype": 9,
			"title": "你的“武功秘籍”到了！"
		},
		"comm_msg_info": {
			"content": "",
			"datetime": 1523768162,
			"fakeid": "3071750887",
			"id": 1000000026,
			"status": 2,
			"type": 49
		}
	}]
}""")
    print(load_all_data)