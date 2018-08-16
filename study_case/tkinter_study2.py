# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/14 11:20
"""
import time
from tkinter import *


class Watch(Frame):
    msec = 1000
    index = 0

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)  # tkinter的初始化
        self.timestr1 = StringVar()
        self.timestr2 = StringVar()
        self.makeWidgets()

    def makeWidgets(self):

        l1 = Label(self, textvariable=self.timestr1)
        l2 = Label(self, textvariable=self.timestr2)
        l1.pack() #pack布局，默认先使用的放到上面，然后依次向下排
        l2.pack()

    def _update(self):
        self._settime()
        # tkinter的root窗口有一个after函数，用于在一定时间后执行一个函数，参数是（毫秒，调用的函数）
        self.timer = self.after(self.msec, self._update)
        # print(self.timer)

    def _settime(self):
        today1 = str('你好' + str(self.index))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)
        self.index += 1

    def start(self):
        self._update()
        self.pack(anchor=CENTER)


if __name__ == '__main__':
    root = Tk()
    root.geometry('250x150')
    mw = Watch(root)
    mw.start()
    root.mainloop()
