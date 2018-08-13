# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/8/13 9:31
'''
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def sina():
    is_first = True
    task_q = [] # 本地存储新闻
    task_time = []
    while True:
        data_list = getNews()

        if is_first:
            task_q = data_list
            for data in data_list:
                print(data['n_time'],data['n_info'])
                time.sleep(0.5)
                task_time.append(data['n_time'])
            is_first = False
        else:
            for data in data_list:
                if data['n_time'] in task_time:
                    pass
                else:
                    task_time.append(data['n_time'])
                    print('-'*30)
                    print('新消息',data['n_time'],data['n_info'])

        time.sleep(5)

def getNews(): # 获取新闻函数
    news_list =[]
    """
    使用selenium可以解决爬取不到js动态生成的代码问题
    """
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get('http://finance.sina.com.cn/7x24/?tag=10')
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source)
    info_list = soup.select('.bd_i_og')
    print(info_list)
    print('----------------------------------------------')

    for info in info_list:  # 获取页面中自动刷新的新闻
        n_time = info.select('p[class="bd_i_time_c"]')[0].get_text()  # 新闻时间及内容
        n_info = info.select('p[class="bd_i_txt_c"]')[0].get_text()
        data = {
            'n_time': n_time,
            'n_info': n_info
        }
        news_list.append(data)
    return news_list[::-1] # 这里倒序，这样打印时才会先打印旧新闻，后打印新新闻

if __name__ == '__main__':
    sina()