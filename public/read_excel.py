# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/15 20:22
"""

import xlrd

from public import config
from public.log import Log


class ReadExcel(object):
    # 参数excel_path是文件的绝对路径，sheet_name是表名
    def __init__(self, excel_path, sheet_name="Sheet1"):
        self.data = xlrd.open_workbook(excel_path)  # 根据路径打开一个文件
        self.table = self.data.sheet_by_name(sheet_name)  # 根据表名打开表
        self.keys = self.table.row_values(0)  # 获取第一行作为字典的key值
        self.rowNum = self.table.nrows  # 获取总行数
        self.colNum = self.table.ncols  # 获取总列数
        self.log = Log("读取excel").get_logger()

    # 获取整张表的数据（数据装在列表中,列表的每个子元素是字典类型数据）
    def get_dict_data(self):
        if self.rowNum <= 1:
            self.log.error('xlsx表的总行数小于1')
        else:
            r = []  # 定义列表变量，把读取的每行数据拼接到此列表中

            for row in range(1, self.rowNum):  # 对行进行循环读取数据，从第二行开始
                s = {}  # 定义字典变量
                s['rowNum'] = row + 1  # 存储行数，从第二行开始读，行数等于下标加1
                values = self.table.row_values(row)  # 获取行的数据

                for col in range(0, self.colNum):  # 对列进行循环读取数据
                    cell_value = values[col]
                    if isinstance(cell_value, (int, float)):  # 判断读取数据是否是整型或浮点型
                        cell_value = int(cell_value)  # 是，数据转换为整数

                    s[self.keys[col]] = str(cell_value).strip()  # 获取到单元格数据(去掉头尾空格)和key组成键对值
                r.append(s)  # 把获取到行的数据装入r列表中
            return r  # 返回整个表的数据


if __name__ == "__main__":
    file_path = config.test_data_path + 'test.xlsx'
    sheetName = "test"
    sheet = ReadExcel(file_path, sheetName)
    data = sheet.get_dict_data()
    print(data[0]['checkpoint'])
    print(type(data[0]['checkpoint']))
    print(data)
