# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
启动jvm
 @Author  : pgsheng
 @Time    : 2018/7/24 10:44
"""
import platform
import jpype
from public.log import Log

class JVMStart(object):

    def __init__(self):
        self.log = Log("jvm初始化").getLog()

    ''' 
    启动Java虚拟机
    '''
    def startJVM(self):
        # 获得默认jvm路径
        jvm_path = jpype.getDefaultJVMPath()
        self.log.info(jvm_path)

        # 你的java扩展包的路径
        ext_classpath = ''

        # 判断系统类型,Linux系统使用“ ：”分隔
        sysstr = platform.system()
        if sysstr == "Windows":
            # java扩展包的路径或class文件所在文件夹路径，注意：class文件路径是它所在的上级文件夹
            ext_classpath = r"C:\AProjectCode\Pycharm-Projects\python3_interface\java\jar_test.jar;C:\AProjectCode\Pycharm-Projects\python3_interface\java"
        elif sysstr == "Linux":
            ext_classpath = r"C:\AProjectCode\Pycharm-Projects\python3_interface\java\jar_test.jar:C:\AProjectCode\Pycharm-Projects\python3_interface\java"
        self.log.info("系统类型：" + sysstr)

        # 判断 JVM 是否已启动
        if not jpype.isJVMStarted():
            # 启动Java虚拟机，并加载jar包
            jpype.startJVM(jvm_path, '-ea', '-Djava.class.path=%s' % ext_classpath)
            jpype.java.lang.System.out.println( "startJVM success!")
            if jpype.isJVMStarted():
                return True
            else:
                return False
        else:
            return True

    ''' 
    关闭Java虚拟机
    '''
    def shutdownJVM(self):
        if jpype.isJVMStarted():
            self.log.info("关闭jvm")
            jpype.shutdownJVM()


if __name__ == '__main__':
    JVMStart().startJVM()
    JVMStart().shutdownJVM()
