"""
 adb实现坐标快速点击
 @Author  : pgsheng
 @Time    : 2018/8/23 8:29
"""
import multiprocessing
import os
from threading import Lock

mutex = Lock()

def test(x, y):
    while True:
        # mutex.acquire()
        os.system('adb shell input tap {} {}'.format(x, y))
        # mutex.release()

if __name__ == '__main__':
    for i in range(10):
        p = multiprocessing.Process(target=test, args=(541, 1606))
        p.start()
