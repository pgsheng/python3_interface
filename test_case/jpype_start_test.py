# !/usr/bin/python3
# -*- coding: utf-8 -*-
'''
测试jpype是否安装成功，可以用
 @Author  : pgsheng
 @Time    : 2018/4/25 21:25
'''
import jpype

jvmPath = jpype.getDefaultJVMPath()       # 默认的JVM路径
print(jvmPath)
jpype.startJVM(jvmPath)
jpype.java.lang.System.out.println("hello world!")
jpype.java.lang.System.out.println("I hate you!")

jpype.shutdownJVM() # 关闭JVM
