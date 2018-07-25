# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
测试jpype是否安装成功，可以用
 @Author  : pgsheng
 @Time    : 2018/4/25 21:25
"""

from jpype import JClass
from public.jvm_start import JVMStart
from public.log import Log

class Jpype_Test():

    def __init__(self):
        self.log = Log().getLog()

    def startJvm(self):
        return JVMStart().startJVM()

    """class文件调用"""
    def get_object_class(self):
        # 获取java的实体类
        JavaClass2 = JClass("JavaClass2")
        # java的实体类使用案例
        javaInstance2 = JavaClass2("哈喽！")  # 实例化对象
        self.log.info(javaInstance2.getValue())  # 调用JAVA对象的方法

    """直接调用JAVA API"""
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
        self.log.debug(unicastPort)
        self.log.debug(type(unicastPort))

    """调用JAVA第三方扩展包"""
    def get_object_jar(self):
        # 获取java的实体类
        JavaClass = JClass("com.jar.test.JavaClass")

        # java的实体类使用案例
        javaInstance = JavaClass("oldvalue")  # 实例化对象
        self.log.info(javaInstance.getValue())  # 调用JAVA对象的方法
        javaInstance.setName("胜")
        self.log.info(javaInstance.name)
        self.log.info(javaInstance.getName())

    def shutdownJVM(self):
        JVMStart().shutdownJVM()


if __name__ == '__main__':
    if Jpype_Test().startJvm():
        Jpype_Test().get_object_class()
        Jpype_Test().get_base_java()
        Jpype_Test().get_object_jar()
        Jpype_Test().shutdownJVM()

"""
实体类的代码

public class JavaClass {
    private String value;
	public String name = "测试";

	public JavaClass(String value) {
		this.value = value;
	}

	public String getValue() {
		return this.value;
	}

	public void setValue(String val) {
		this.value = val;
	}

	public String getName() {
		return this.name;
	}

	public void setName(String name) {
		this.name = name;
	}
}
"""
