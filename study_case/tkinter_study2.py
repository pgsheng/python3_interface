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
        Frame.__init__(self, parent, kw)
        self._running = False
        self.timestr1 = StringVar()
        self.timestr2 = StringVar()
        self.makeWidgets()
        self.flag = True

    def makeWidgets(self):
        l1 = Label(self, textvariable=self.timestr1)
        l2 = Label(self, textvariable=self.timestr2)
        l1.pack()
        l2.pack()

    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)

    def _settime(self):
        today1 = str('你好' + str(self.index))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)
        self.index += 1

    def start(self):
        self._update()
        self.pack(side=BOTTOM)


if __name__ == '__main__':
    root = Tk()
    root.geometry('250x150')
    mw = Watch(root)
    mw.start()
    root.mainloop()
