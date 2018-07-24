# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
测试jpype是否安装成功，可以用
 @Author  : pgsheng
 @Time    : 2018/4/25 21:25
'''
from jpype import JClass

from public.jvm_start import JVM_Start
from public.log import Log


class Jpype_Test():

	def __init__(self):
		self.log = Log().getLog()

	def startJvm(self):
		JVM_Start().startJVM()

	def get_base_java(self):
		# 获取java的基本类型类
		System = JClass("java.lang.System")
		String = JClass("java.lang.String")
		Boolean = JClass("java.lang.Boolean")
		Byte = JClass("java.lang.Byte")
		Short = JClass("java.lang.Short")
		Integer = JClass("java.lang.Integer")
		Long = JClass("java.lang.Long")
		Float = JClass("java.lang.Float")
		Double = JClass("java.lang.Double")

		# java的基本类型类使用案例
		unicastPort = String.valueOf(6868)  # int转string类型
		self.log.debug(type(unicastPort))

	def get_object_java(self):
		# 获取java的实体类
		System = JClass("java.lang.System")

		# java的实体类使用案例

		self.log.debug(type())

	def shutdownJVM(self):
		JVM_Start().shutdownJVM()


if __name__ == '__main__':
	Jpype_Test().startJvm()
	Jpype_Test().get_base_java()

	Jpype_Test().shutdownJVM()
