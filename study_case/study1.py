"""
 @Author  : pgsheng
 @Time    : 2019/4/4 15:16
"""
import time

def b(func):
    print(time.ctime())
    return func()

@b  # 从这里可以看出@b 等价于 b(xxx()),但是这种写法你得考虑python代码的执行顺序
def a():
    print('Hello world!')