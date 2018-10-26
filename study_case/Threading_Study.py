# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/24 14:15
"""
import threading
import time

from public.log import Log


class ThreadingStudy(object):

    def __init__(self):
        self.log = Log().get_logger()

    def test(self, t=0):
        print('thread %s is running...' % threading.current_thread().name)
        for i in range(5):
            time.sleep(2)
            self.log.info(t)
        print('thread %s is ended...' % threading.current_thread().name)


if __name__ == '__main__':
    print('thread %s is running...' % threading.current_thread().name)
    tt = []
    t2 = threading.Thread(target=ThreadingStudy().test, args=(1,)) # 注意方法不能带括号
    t = threading.Thread(target=ThreadingStudy().test, args=(2,))
    tt.append(t)
    tt.append(t2)
    # t.setDaemon(True)
    # t2.setDaemon(True)
    for i in tt:
        i.start()

    for i in tt:
        i.join()
    print('thread %s is ended...' % threading.current_thread().name)

"""
默认情况下主程序会等子线程全部执行完毕才停止的。
join()方法：设置主程序会等子线程全部执行完毕才后，才可以接着往下执行，join([timeout]) 里面的参数时可选的，代表线程运行的最大时
     间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会接着执行的，如果线程执行时间小于参数表示的
     时间，则接着执行，不用一定要等待到参数表示的时间。
setDaemon()方法：设置子线程为后台线程，使主线程不等待子线程，主线程结束则全部结束，必须在start() 方法调用之前设置
"""
