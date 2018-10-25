# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/25 21:25
"""

from jpype import JClass

from public.jvm_start import JVMStart
from public.log import Log


class PdfJar(object):

    def __init__(self):
        self.log = Log().get_logger()
        self.path = r'C:\AProjectCode\Python\python3_interface\study_case\data\开发指南.pdf'
        self.out_path = r'C:\AProjectCode\Python\python3_interface\study_case\data\开发指南.txt'

    def startJvm(self):
        return JVMStart().start_jvm(['pdfbox-app-2.0.12.jar'])

    def get_java_objecj(self):
        self.file = JClass("java.io.File")
        self.FileOutputStream = JClass("java.io.FileOutputStream")
        self.OutputStreamWriter = JClass("java.io.OutputStreamWriter")
        self.Writer = JClass("java.io.Writer")
        self.PDDocument = JClass("org.apache.pdfbox.pdmodel.PDDocument")
        self.PDFTextStripper = JClass("org.apache.pdfbox.text.PDFTextStripper")

    def get_txt(self):
        try:
            self.get_java_objecj()
            input = self.file(self.path)  # 转换文件为File类型
            document = self.PDDocument.load(input)  # 加载pdf文件
            outputStream = self.FileOutputStream(self.out_path)
            output = self.OutputStreamWriter(outputStream, 'UTF-8') # 文件输出流
            stripper = self.PDFTextStripper() #  PDFTextStripper来提取文本
            stripper.setSortByPosition(False)  # 设置是否排序
            stripper.setStartPage(1)  # 设置起始页
            stripper.setEndPage(100000)  # 设置结束页
            stripper.writeText(document, output)  # 调用PDFTextStripper的writeText提取并输出文本
            self.log.info(stripper.getText(document) )# 直接获取text

            output.close()  # 关闭输出流
            document.close()
        except Exception as e:
            self.log.error('出现异常：%s' % e)

    def shutdownJVM(self):
        JVMStart().shutdown_jvm()


if __name__ == '__main__':
    p = PdfJar()
    if p.startJvm():
        p.get_txt()
