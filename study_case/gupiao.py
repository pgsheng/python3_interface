import re

import requests
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'shuju')
        panel = wx.Panel(self)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)

        lists = 'sz002626,sh600928'  # sh，sz分别为沪深代码
        res = requests.get('http://hq.sinajs.cn/list=%s' % lists)
        message = re.compile('"(.*)"').findall(res.text)
        for msg in message:
            msg_list = re.split('[，,、]', msg)
            print(msg_list)
            name = msg_list[0]  # 企业名称
            zuotian = '%.2f' % float(msg_list[2])  # 昨天收
            kaipai = '%.2f' % float(msg_list[1])  # 今天开
            dangqian = '%.2f' % float(msg_list[3])  # 当前
            zuigao = '%.2f' % float(msg_list[4])  # 最高
            zuidi = '%.2f' % float(msg_list[5])  # 最低
            jine = '%.0f' % (float(msg_list[9]) / 10000)  # 成交额
            baifenbi = '%.2f' % ((float(dangqian) - float(zuotian)) / float(zuotian) * 100)  # 幅度

            st_list = [name, zuotian, kaipai ,dangqian, zuigao, zuidi, jine, baifenbi]
            horizontal_user = wx.BoxSizer(wx.HORIZONTAL)  # 容器中控件按横向并排排列
            for st in st_list:
                box = wx.StaticText(panel, label=str(st))
                horizontal_user.Add(box, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL, border=5)
            vsizer_all.Add(horizontal_user)
        panel.SetSizer(vsizer_all)
        # Timer(20, self.show_wain).start()

    def show_wain(self):
        wx.MessageBox('dfdf')  # 弹出提示框


if __name__ == '__main__':
    app = wx.App()  # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法


# 0：”大秦铁路”，股票名字；
# 1：”27.55″，今日开盘价；
# 2：”27.25″，昨日收盘价；
# 3：”26.91″，当前价格；
# 4：”27.55″，今日最高价；
# 5：”26.20″，今日最低价；
# 6：”26.91″，竞买价，即“买一”报价；
# 7：”26.92″，竞卖价，即“卖一”报价；
# 8：”22114263″，成交的股票数，由于股票交易以一百股为基本单位，所以在使用时，通常把该值除以一百；
# 9：”589824680″，成交金额，单位为“元”，为了一目了然，通常以“万元”为成交金额的单位，所以通常把该值除以一万；
# 10：”4695″，“买一”申请4695股，即47手；
# 11：”26.91″，“买一”报价；
# 12：”57590″，“买二”
# 13：”26.90″，“买二”
# 14：”14700″，“买三”
# 15：”26.89″，“买三”
# 16：”14300″，“买四”
# 17：”26.88″，“买四”
# 18：”15100″，“买五”
# 19：”26.87″，“买五”
# 20：”3100″，“卖一”申报3100股，即31手；
# 21：”26.92″，“卖一”报价
# (22, 23), (24, 25), (26,27), (28, 29)分别为“卖二”至“卖四的情况”
# 30：”2008-01-11″，日期；
# 31：”15:05:32″，时间；