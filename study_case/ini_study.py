# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/17 9:02
"""
from configparser import ConfigParser


def read_ini():
    config = ConfigParser()
    config.read('C:\AProjectCode\Python\python3_interface\study_case\data\config.ini',encoding="utf-8")
    a = config.get("ZIP", "MD5")
    # a = config["ZIP"]["MD5"]
    print(a)


def write_yaml():
    config = ConfigParser()
    config.add_section("book")
    config.set("book", "title", "the python standard library")
    config.set("book", "author", "fredrik lundh")
    # a追加写入，w覆盖写入
    config.write(open('C:\AProjectCode\Python\python3_interface\study_case\data\config.ini', "a"))


if __name__ == '__main__':
    read_ini()
    # write_yaml()
