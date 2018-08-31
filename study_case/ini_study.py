# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
"""
from configparser import ConfigParser


def read_ini():
    config = ConfigParser()
    config.readfp(
        open('C:\AProjectCode\Pycharm-Projects\python3_interface\study_case\data\config.ini'))
    a = config.get("ZIP", "MD5")
    print(a)


def write_yaml():
    config = ConfigParser()
    config.add_section("book")
    config.set("book", "title", "the python standard library")
    config.set("book", "author", "fredrik lundh")
    # config.add_section("ematter")
    # config.set("ematter", "pages", '250')
    # write to file
    # a追加写入，w覆盖写入
    config.write(open('C:\AProjectCode\Pycharm-Projects\python3_interface\study_case\data\config.ini', "r+"))


if __name__ == '__main__':
    read_ini()
    # write_yaml()
