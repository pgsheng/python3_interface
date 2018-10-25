# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/10/24 14:15
"""
import io
from io import StringIO

from pdfminer.converter import PDFPageAggregator, TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfparser import PDFParser, PDFDocument

from public.log import Log
"""
pip install pdfminer3k
"""

class Pdf(object):

    def __init__(self):
        self.log = Log().get_logger()
        self.path = r'C:\AProjectCode\Python\python3_interface\study_case\data\开发指南.pdf'
        # self.path = r'C:\AProjectCode\Python\python3_interface\study_case\data\a.pdf'
        self.out_path = r'C:\AProjectCode\Python\python3_interface\study_case\data\aa.txt'

    def read(self):
        with open(self.path, 'rb') as fp:  # 以二进制读模式打开
            praser = PDFParser(fp)  # 用文件对象来创建一个pdf文档分析器
            retstr = StringIO()
            doc = PDFDocument()  # 创建一个PDF文档
            praser.set_document(doc)  # 连接分析器 与文档对象
            doc.set_parser(praser)  # 获取解析内容
            doc.initialize()  # 提供初始化密码，如果没有密码就创建一个空的字符串
            if not doc.is_extractable:  # 检测文档是否提供txt转换
                self.log.info("文档不可以进行txt转换")
            else:
                rsrcmgr = PDFResourceManager()  # 创建PDf 资源管理器 来管理共享资源
                laparams = LAParams()  # 创建一个PDF设备对象
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                interpreter = PDFPageInterpreter(rsrcmgr, device)  # 创建一个PDF解释器对象
                with open(self.out_path, 'w', encoding='utf-8') as f:
                    # 循环遍历列表，每次处理一个page的内容
                    for page in doc.get_pages():  # doc.get_pages() 获取page列表
                        interpreter.process_page(page)
                        layout = device.get_result()  # 接受该页面的LTPage对象
                        # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性，
                        for x in layout:
                            if hasattr(x,'get_text'):
                                results = x.get_text()
                                self.log.info(results)
                                f.write(results)

    def read2(self):
        pdfFile = open(r'C:\AProjectCode\Python\python3_interface\study_case\data\开发指南.pdf', 'rb')
        retstr = io.StringIO()
        laparams = LAParams()
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device, pdfFile, pagenos=set(), maxpages=0, password='',
                    check_extractable=True)
        device.close()
        print(retstr.getvalue())
        pdfFile.close()
if __name__ == '__main__':
    Pdf().read2()
