# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/14 11:20
"""
import time
from tkinter import *


def test1():
    root = Tk()
    root.geometry('250x150')
    timestr1 = StringVar()
    l1 = Label(root, textvariable=timestr1)
    time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
    timestr1.set(time1)
    l1.pack()  # pack布局，默认先使用的放到上面，然后依次向下排
    root.after(1000, test1)
    root.mainloop()


def _update(self):
    self._settime()
    # tkinter的root窗口有一个after函数，用于在一定时间后执行一个函数，参数是（毫秒，调用的函数）
    self.timer = self.after(self.msec, self._update)


def settime(timestr1,):
    time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
    timestr1.set(time1)


if __name__ == '__main__':
   test1()