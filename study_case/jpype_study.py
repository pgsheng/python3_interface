# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/25 21:25
"""

from jpype import JClass
from public.jvm_start import JVMStart
from public.log import Log


class JpypeTest(object):

    def __init__(self):
        self.log = Log().get_logger()

    def startJvm(self):
        return JVMStart().start_jvm(['jar_test.jar'])

    """class文件调用"""

    def get_object_class(self):
        # 获取java的实体类
        java_class = JClass("JavaClass2")
        # java的实体类使用案例
        java_instance = java_class("哈喽！")  # 实例化对象
        self.log.info(java_instance.getValue())  # 调用JAVA对象的方法

    """直接调用JAVA API"""

    def get_base_java(self):
        # 获取java的基本类型类
        system = JClass("java.lang.System")
        string = JClass("java.lang.String")
        Boolean = JClass("java.lang.Boolean")
        Byte = JClass("java.lang.Byte")
        Short = JClass("java.lang.Short")
        Integer = JClass("java.lang.Integer")
        Long = JClass("java.lang.Long")
        Float = JClass("java.lang.Float")
        Double = JClass("java.lang.Double")

        # java的基本类型类使用案例
        port = string.valueOf(6868)  # int转string类型
        self.log.debug(port)
        self.log.debug(type(port))

    """调用JAVA第三方扩展包"""

    def get_object_jar(self):
        # 获取java的实体类
        java_class = JClass("com.jar.test.JavaClass")

        # java的实体类使用案例
        java_instance = java_class("oldvalue")  # 实例化对象
        self.log.info(java_instance.getValue())  # 调用JAVA对象的方法
        java_instance.setName("胜")
        self.log.info(java_instance.name)
        self.log.info(java_instance.getName())

    def shutdownJVM(self):
        JVMStart().shutdown_jvm()


if __name__ == '__main__':
    if JpypeTest().startJvm():
        JpypeTest().get_object_class()
        JpypeTest().get_base_java()
        JpypeTest().get_object_jar()
        JpypeTest().shutdownJVM()

