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
            # name_st = wx.StaticText(panel, label=name)
            # zuotian_st = wx.StaticText(panel, label=zuotian)
            # kaipai_st = wx.StaticText(panel, label=kaipai)
            # dangqian_st = wx.StaticText(panel, label=dangqian)
            # zuigao_st = wx.StaticText(panel, label=zuigao)
            # zuidi_st = wx.StaticText(panel, label=zuidi)
            # jine_st = wx.StaticText(panel, label=str(jine))
            # baifenbi = wx.StaticText(panel, label=str(baifenbi))
                horizontal_user.Add(box, proportion=1, flag=wx.ALIGN_CENTER_VERTICAL, border=5)
                # horizontal_user.Add(zuotian_st)
                # horizontal_user.Add(kaipai_st)
                # horizontal_user.Add(dangqian_st)
                # horizontal_user.Add(zuigao_st)
                # horizontal_user.Add(zuidi_st)
                # horizontal_user.Add(jine_st)
                # horizontal_user.Add(baifenbi)
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
