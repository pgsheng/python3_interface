"""
 @Author  : pgsheng
 @Time    : 2018/3/7 15:24
"""
import logging
import time
import os

from public import config


class Log(object):
    """日志类"""

    def __init__(self, name=None):
        day = time.strftime("%Y%m%d", time.localtime(time.time()))  # 获取当前时间
        file = os.path.join(config.test_log_path, (day + '.log'))  # 以当前时间命名日志文件
        self.logger = logging.Logger(name)  # 定义日志的名称
        self.logger.setLevel(logging.DEBUG)  # 设置日志等级
        self.logfile = logging.FileHandler(file, encoding="UTF-8")  # 定义日志输出到文件
        self.logfile.setLevel(logging.DEBUG)  # 将INFO级别或更高的日志输出到文件
        self.control = logging.StreamHandler()  # 定义日志输出到控制台
        self.control.setLevel(logging.DEBUG)  # 将INFO级别或更高的日志输出到控制台
        # 定义日志格式:时间、文件名、行号、标记、结果
        self.formater = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d : %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)
        self.logfile.close()
        self.control.close()

    def get_logger(self):
        return self.logger
