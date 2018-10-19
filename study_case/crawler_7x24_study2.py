# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/13 9:31
"""
import time

import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from public import config


class Sina_7x24():

    def __init__(self):
        self.is_first = True
        self.task_time = []
        self.task_info = []

    def _sina(self):
        data_list = self._news()

        if self.is_first:
            for data in data_list:
                self.task_time.append(data['n_time'])
                self.task_info.append(data['n_info'])
                print(data['n_time'], data['n_info'])
                time.sleep(0.1)
            self.is_first = False
        else:
            for data in data_list:
                if data['n_time'] in self.task_time:
                    pass
                else:
                    self.task_time.append(data['n_time'])
                    self.task_info.append(data['n_info'])
                    print('-' * 30)
                    print('新消息', data['n_time'], data['n_info'])

        total = {'Time': self.task_time[::-1], 'Content': self.task_info[::-1]}
        # ( 运行起始点 )用pandas模块处理数据并转化为excel文档
        df = pandas.DataFrame(total)
        df.to_excel(config.study_case_path + r'data\7x24_2.xlsx', 'Sheet1')

        time.sleep(3)
        self._sina()  # 每隔 N 秒跑一次

    def _news(self):  # 获取新闻函数
        news_list = []
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        info_list = soup.select('.bd_i_og')
        for info in info_list:  # 获取页面中自动刷新的新闻
            n_time = info.select('p.bd_i_time_c')[0].text  # 新闻时间及内容
            n_info = info.select('p.bd_i_txt_c')[0].text
            data = {
                'n_time': n_time,
                'n_info': n_info
            }
            news_list.append(data)
        return news_list[::-1]  # 这里倒序，这样打印时才会先打印旧新闻，后打印新新闻

    def start(self):
        """
          用selenium可以解决爬取不到js动态生成的代码问题
        """
        options = Options()
        options.add_argument('-headless')  # 无界面配置
        self.browser = webdriver.Firefox(firefox_options=options)
        # self.browser = webdriver.Ie()
        self.browser.get('http://finance.sina.com.cn/7x24/')
        time.sleep(1)
        self._sina()


if __name__ == '__main__':
    mw = Sina_7x24()
    mw.start()
