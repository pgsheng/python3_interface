import multiprocessing
import os
from threading import Lock

"""
实现某个坐标快速连接点击
"""
mutex = Lock()

def test(x, y):
    while True:
        # mutex.acquire()
        os.system('adb shell input tap {} {}'.format(x, y))
        # mutex.release()


if __name__ == '__main__':
    # for i in range(4):
    #     t = Thread(target=test, args=(541,1606))
    #     t.start()

    for i in range(10):
        p = multiprocessing.Process(target=test, args=(541, 1606))
        p.start()