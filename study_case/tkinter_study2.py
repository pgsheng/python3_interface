# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
 @Author  : pgsheng
 @Time    : 2018/8/14 11:20
'''
from tkinter import *
import time


class StopWatch(Frame):
    '''实现一个秒表部件'''
    msec = 50
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
        self.flag  = True
    def makeWidgets(self):
        '''制作时间标签'''
        l = Label(self, textvariable = self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill = X, expand = NO, pady = 2, padx = 2)
    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(self.msec, self._update)
    def _setTime(self, elap):
        '''将时间格式改为 分：秒：百分秒'''
        minutes = int(elap/60)
        seconds = int(elap-minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds) *100)
        self.timestr.set('%2d:%2d:%2d' %(minutes, seconds, hseconds))
    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True
    def Stop(self):
        '''停止秒表'''
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = False
    def Reset(self):
        '''重设秒表'''
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


    def stopwatch(self):
        if self.flag == True:
            self.pack(side = TOP)
            Button(self, text = 'start', command = self.Start).pack(side = LEFT)
            Button(self, text = 'stop', command = self.Stop).pack(side = LEFT)
            Button(self, text = 'reset', command = self.Reset).pack(side = LEFT)
            Button(self, text = 'quit', command = self.quit).pack(side = LEFT)
        self.flag = False



class Watch(Frame):
    msec = 1000
    def __init__(self, parent=None, **kw):
            Frame.__init__(self, parent, kw)
            self._running = False
            self.timestr1 = StringVar()
            self.timestr2 = StringVar()
            self.makeWidgets()
            self.flag  = True
    def makeWidgets(self):
        l1 = Label(self, textvariable = self.timestr1)
        l2 = Label(self, textvariable = self.timestr2)
        l1.pack()
        l2.pack()
    def _update(self):
        self._settime()
        self.timer = self.after(self.msec, self._update)
    def _settime(self):
        today1 = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
        time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
        self.timestr1.set(today1)
        self.timestr2.set(time1)
    def start(self):
        self._update()
        self.pack(side = TOP)

if __name__ == '__main__':
    def main():
        root = Tk()
        root.geometry('250x150')
        frame1 = Frame(root)
        frame1.pack(side = BOTTOM)
        sw = StopWatch(root)
        stpwtch = Button(frame1, text = '秒表', command = sw.stopwatch)
        stpwtch.pack(side = RIGHT)
        mw = Watch(root)
        mywatch = Button(frame1, text = '时钟', command = mw.start)
        mywatch.pack(side = LEFT)
        root.mainloop()
    main()