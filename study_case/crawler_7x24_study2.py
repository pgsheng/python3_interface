# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/13 9:31
"""
import time
from tkinter import Frame, StringVar, Label, Tk, CENTER, E, Listbox

import pandas
from bs4 import BeautifulSoup
from selenium import webdriver

from public import config


class Sina_7x24(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)  # tkinter的初始化
        self.is_first = True
        self.task_time = []
        self.task_info = []
        self.timestr = StringVar()
        l = Label(self,
                  width=250,
                  height=150,
                  wraplength=250,
                  justify='left',
                  textvariable=self.timestr)
        self.display_info = Listbox(self, width=240)
        l.pack()
        self.display_info.pack()

    def sina(self):
        data_list = self.getNews()

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
                    print('新消息', data['n_time'], data['n_info'])

        tk_list = data_list[::-1]
        self.timestr.set(tk_list[0].get('n_info'))
        self.pack(anchor=E)

        self.after(15000, self.sina)

    def getNews(self):  # 获取新闻函数
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
               使用selenium可以解决爬取不到js动态生成的代码问题
        """
        # browser = webdriver.Firefox()
        self.browser = webdriver.Ie()
        self.browser.minimize_window()
        self.browser.get('http://finance.sina.com.cn/7x24/')
        time.sleep(1)
        self.sina()


if __name__ == '__main__':
    root = Tk()
    root.geometry('250x150')
    mw = Sina_7x24(root)
    mw.start()
    root.mainloop()
