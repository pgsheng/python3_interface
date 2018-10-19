# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/12 17:15
"""
import json
import sys

import pandas as pandas
import requests
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from bs4 import BeautifulSoup
from public import config


def test1():
    title_all = []
    article_all = []
    url_all = []
    date_all = []

    res = requests.get('http://news.sina.com.cn/china/') #requests爬取不到js动态生成的代码
    res.encoding = 'utf-8'
    # 将requests获取的网页信息转换为BeautifulSoup的物件存于soup中，并指明其剖析器为'html.parser'
    soup = BeautifulSoup(res.text, 'html.parser')

    # 用beautifulSoup中的select方法可以获取相应的元素，且获取的元素为list形式
    news = soup.select('.news-1')[0].select('a')
    print(news)
    for new in news:
        url = new['href']
        title = new.text
        print(url)
        print(title)
    # for new in soup.select('.news-item'):  # 获取所有class为news-item的
    #     if len(news.select('h2')) > 0:
    #         print(news)
    #         # h2 = news.select('h2')[0].text
    #         # time = news.select('.time')[0].text
    #         url = news.select('a')[0]['href']
    #
    #         # test2(url)
    #         res2 = requests.get(url)
    #         res2.encoding = 'utf-8'
    #         soup2 = BeautifulSoup(res2.text, 'html.parser')
    #
    #         if len(soup2.select('.main-title')) <= 0:
    #             continue
    #         title = soup2.select('.main-title')[0].text
    #         date = soup2.select('span.date')[0].contents[0]
    #         article = []
    #         # 循环id为article下的所有p标签,不包含最后一个
    #         for p in soup2.select('#article p')[:-1]:
    #             article.append(p.text.strip())
    #
    #         title_all.append(title)
    #         date_all.append(date)
    #         article_all.append(article)
    #         url_all.append(url)
    #
    #         print(title)
    #         print(date)
    #         print(article)
    #         print(url)
    #
    # total = {'a_title': title_all, 'b_article': article_all, 'url_all': url_all,
    #          'date_all': date_all}
    # # ( 运行起始点 )用pandas模块处理数据并转化为excel文档
    #
    # df = pandas.DataFrame(total)
    # df.to_excel(config.study_case_path + r'data\news.xlsx','Sheet1')
    # print(total)


def test2(url=None):
    # res = requests.get(url)
    res = requests.get('http://news.sina.com.cn/c/nd/2018-04-11/doc-ifyteqtq7576205.shtml')
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    if len(soup.select('.main-title')) <= 0:
        return

    # 抓标题
    print(soup.select('.main-title')[0].text)

    # 日期
    print(soup.select('span.date')[0].contents[0])  # span标签class为date
    # print(soup.select('span.date')[0].text)  # span标签class为date
    # print(soup.select('.date-source span')[0].text)  # class为date-source下的span标签

    article = []
    # 循环id为article下的所有p标签,不包含最后一个
    for p in soup.select('#article p')[:-1]:
        article.append(p.text.strip())
    print(article)
    # print(' \n'.join(article))  # 将article列表中的每一项用换行符‘ \n ’分隔开

    print(soup.select('.show_author')[0].text)
    # print(soup.select('.show_author')[0].text.lstrip('责任编辑：'))  # 过滤'责任编辑：'


def test3():
    # 评论接口
    res = requests.get(
        'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=comos-hhqtawx2681362&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3&t_size=3&h_size=3&thread=1&callback=jsonp_1534068718135&_=1534068718135')
    res.encoding = 'utf-8'
    print(res.text)
    # 把获取的内容转化为json格式读取python字典
    jd = json.loads(res.text.strip('jsonp_1534068718135(').rstrip(')'))
    print(jd)
    print(jd['result']['count']['total'])

class Render(QWebEnginePage):
    def __init__(self,url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def test4():
    url = 'http://finance.sina.com.cn/7x24/'
    r = Render(url)
    soup = BeautifulSoup(r.html, 'lxml')
    info_list = soup.select('.bd_i_og')

    for info in info_list:  # 获取页面中自动刷新的新闻
        n_time = info.select('p.bd_i_time_c')[0].text  # 新闻时间及内容
        n_info = info.select('p.bd_i_txt_c')[0].text
        print(n_time)
        print(n_info)

if __name__ == '__main__':
    test1()
    # test2()
    # test3()
    # test4()
