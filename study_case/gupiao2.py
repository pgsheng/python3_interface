import os
import re
import time
from tkinter import messagebox, mainloop

import requests


class GuPiao():
    def __init__(self):
        self.values = 'sz002626,sh600928'  # sh，sz分别为沪深代码

    def get_data(self):
        while True:
            res = requests.get('http://hq.sinajs.cn/list=%s' % self.values)
            message = re.compile('"(.*)"').findall(res.text)
            for msg in message:
                msg_list = re.split('[，,、]', msg)
                # print(msg_list)
                name = msg_list[0][0:2]  # 企业名称
                zuotian = '%.2f' % float(msg_list[2])  # 昨天收
                kaipai = '%.2f' % float(msg_list[1])  # 今天开
                dangqian = '%.2f' % float(msg_list[3])  # 当前
                zuigao = '%.2f' % float(msg_list[4])  # 最高
                zuidi = '%.2f' % float(msg_list[5])  # 最低
                jine = '%.2f' % (float(msg_list[9]) / 100000000)  # 成交额(亿)
                baifenbi = '%.2f' % (
                        (float(dangqian) - float(zuotian)) / float(zuotian) * 100)  # 幅度
                # st_list = [name, zuotian, kaipai, dangqian, zuigao, zuidi, jine, baifenbi]
                # show = name + ':' + zuotian + ',' + kaipai + ',' + dangqian + ',' + zuotian + ',' + zuigao + ',' + zuidi + ',' + jine + ',' + baifenbi
                show = name + ':' + dangqian + ',' + baifenbi + ',' + '[高:' +  zuigao + ',' + '低:' + zuidi + ']'
                print(show)
                if abs(float(baifenbi)) > 1:
                    self.show_wain(name + '：' + baifenbi)
            time.sleep(5)

    def show_wain(self, msg):
        messagebox.showerror("", msg)


if __name__ == '__main__':
    g = GuPiao()
    g.get_data()
