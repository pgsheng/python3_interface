'''
 @Author  : pgsheng
 @Time    : 2018/3/7 15:24
'''

import os, time, logging

from public import Config


class Log():
	'''日志类'''

	def __init__(self, name=None):
		day = time.strftime("%Y%m%d%H", time.localtime(time.time()))  # 获取当前时间
		file_dir = Config.project_path + '\\test_log'  # 定义日志文件存储路径
		file = os.path.join(file_dir, (day + '.log'))  # 以当前时间命名日志文件
		self.logger = logging.Logger(name)  # 定义日志的名称
		self.logger.setLevel(logging.INFO)  # 设置日志等级
		self.logfile = logging.FileHandler(file, encoding="UTF-8")  # 定义日志输出到文件
		self.logfile.setLevel(logging.INFO)  # 将INFO级别或更高的日志输出到文件
		self.control = logging.StreamHandler()  # 定义日志输出到控制台
		self.control.setLevel(logging.INFO)  # 将INFO级别或更高的日志输出到控制台
		# 定义日志格式:时间、文件名、行号、标记、结果
		self.formater = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(name)s : %(message)s')
		self.logfile.setFormatter(self.formater)
		self.control.setFormatter(self.formater)
		self.logger.addHandler(self.logfile)
		self.logger.addHandler(self.control)

	def getLog(self):
		return self.logger
