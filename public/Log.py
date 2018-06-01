'''
 @Author  : pgsheng
 @Time    : 2018/3/7 15:24
'''

import os, time, logging

from public import Config


class Log():
	'''日志类'''

	def __init__(self, name='接口测试'):
		day = time.strftime("%Y%m%d%H", time.localtime(time.time()))  # 获取当前时间
		file_dir = Config.project_path + '\\test_log'  # 定义日志文件存储路径
		file = os.path.join(file_dir, (day + '.log'))  # 以当前时间命名日志文件
		self.logger = logging.Logger(name)  # 定义日志的名称
		self.logger.setLevel(logging.INFO)  # 设置日志等级
		self.logfile = logging.FileHandler(file, encoding="UTF-8")  # 定义日志输出到文件
		self.logfile.setLevel(logging.INFO)  # 将INFO级别或更高的日志输出到文件
		self.control = logging.StreamHandler()  # 定义日志输出到控制台
		self.control.setLevel(logging.INFO)  # 将INFO级别或更高的日志输出到控制台
		# 定义日志格式:时间、名称、级别、结果
		self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		self.logfile.setFormatter(self.formater)
		self.control.setFormatter(self.formater)
		self.logger.addHandler(self.logfile)
		self.logger.addHandler(self.control)

	def info(self, message):
		self.logger.info(message)

	def debug(self, message):
		self.logger.debug(message)

	def warning(self, message):
		self.logger.warning(message)

	def error(self, message):
		self.logger.error(message)
