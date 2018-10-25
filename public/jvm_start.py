# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
启动jvm
 @Author  : pgsheng
 @Time    : 2018/7/24 10:44
"""
import platform

import jpype

from public import config
from public.log import Log


class JVMStart(object):

    def __init__(self):
        self.log = Log("jvm初始化").get_logger()

    """ 
    启动Java虚拟机
    """

    def start_jvm(self, jar_list):
        # 获得默认jvm路径
        jvm_path = jpype.getDefaultJVMPath()
        # self.log.info(jvm_path)

        # 你的java扩展包的路径
        ext_classpath = ''

        # 判断系统类型,Linux系统使用“ ：”分隔
        sysstr = platform.system()
        if sysstr == "Windows":
            # java扩展包的路径或class文件所在文件夹路径，注意：class文件路径是它所在的上级文件夹
            ext_classpath = config.sdk_path
            for name in jar_list:
                ext_classpath += ';' + config.sdk_path + '%s' % name
        elif sysstr == "Linux":
            ext_classpath = config.sdk_path + 'sdk'
            for name in jar_list:
                ext_classpath = ':' + config.sdk_path + '%s' % name
        # self.log.info("系统类型：" + sysstr)

        # 判断 JVM 是否已启动
        if not jpype.isJVMStarted():
            # 启动Java虚拟机，并加载jar包
            jpype.startJVM(jvm_path, '-ea', '-Djava.class.path=%s' % ext_classpath)
            jpype.java.lang.System.out.println("startJVM success!")
            if jpype.isJVMStarted():
                return True
            else:
                return False
        else:
            return True

    """ 
    关闭Java虚拟机
    """

    def shutdown_jvm(self):
        if jpype.isJVMStarted():
            self.log.info("关闭jvm")
            jpype.shutdownJVM()


if __name__ == '__main__':
    JVMStart().start_jvm(['jar_test.jar'])
    JVMStart().shutdown_jvm()

"""
jpype安装教程：https://www.jianshu.com/p/a701f021df1d
"""
