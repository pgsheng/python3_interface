# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
启动jvm
 @Author  : pgsheng
 @Time    : 2018/7/24 10:44
'''
import platform
import jpype

from public.log import Log


class JVM_Start():

	def __init__(self):
		self.log = Log("jvm初始化").getLog()

	''' 
	启动Java虚拟机
	'''

	def startJVM(self):
		# 获得默认jvm路径
		jvmPath = jpype.getDefaultJVMPath()
		self.log.info(jvmPath)
		# 你的java扩展包的路径
		ext_classpath = ''

		# 判断系统类型,Linux系统使用“ ：”分隔
		sysstr = platform.system()
		if (sysstr == "Windows"):
			# 你的java扩展包的路径
			ext_classpath = r'lib/logback-core-1.1.7.jar;lib/logback-classic-1.1.7.jar'
		elif (sysstr == "Linux"):
			# 你的java扩展包的路径
			ext_classpath = r'lib/logback-core-1.1.7.jar:lib/logback-classic-1.1.7.jar'
		self.log.info("系统类型：" + sysstr)

		# 判断 JVM 是否已启动
		if not jpype.isJVMStarted():
			# 启动Java虚拟机，并加载jar包
			jpype.startJVM(jvmPath, '-ea', '-Djava.class.path=%s' % ext_classpath)
			jpype.java.lang.System.out.println("startJVM success")

	''' 
	关闭Java虚拟机
	'''

	def shutdownJVM(self):
		if jpype.isJVMStarted():
			self.log.info("关闭jvm")
			jpype.shutdownJVM()



if __name__ == '__main__':
	JVM_Start().startJVM()
	JVM_Start().shutdownJVM()
