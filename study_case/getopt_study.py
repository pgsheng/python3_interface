# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/7/25 11:17
"""
import getopt
import sys


"""
1. 使用控制台执行（注意文件路径），如：python getopt_study.py -h 或 python getopt_study.py --help
2. 使用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）。
3. 使用短格式分析串"hf:"，也可以写成'-h-f:'，。当一个选项只是表示开关状态时，即后面不带附加参数时，在分析串中写入选项字符。
    当选项后面是带一个附加参数时，在分析串中写入选项字符同时后面加一个":"号。所以"hf:"就表示"h"是一个开关选项；
    "f:"则表示后面应该带一个参数。
4. 使用长格式分析串列表：["help", "output="]。长格式串也可以有开关状态，即后面不跟"="号。
    如果跟一个等号则表示后面还应有一个参数。这个长格式表示"help"是一个开关选项；"output="则表示后面应该带一个参数。
5. 调用getopt函数。函数返回两个列表：opts和args。opts为分析出的格式信息。args为不属于格式信息的剩余的命令行参数,
    即不是按照getopt(）里面定义的长或短选项字符和附加参数以外的信息。opts是一个两元组的列表。
    每个元素为：(选项串,附加参数)。如果没有附加参数则为空串''。
"""
opts, args = getopt.getopt(sys.argv[1:], '-h-f:-v', ['help', 'name=', 'version'])
print(opts)
for opt_name, opt_value in opts:
    if opt_name in ('-h', '--help'):
        print("Help info")
        sys.exit()
    if opt_name in ('-v', '--version'):
        print("Version is 0.01")
        sys.exit()
    if opt_name in ('-f', '--name'):
        fileName = opt_value
        print("Filename is", fileName)
        # do something
        sys.exit()
