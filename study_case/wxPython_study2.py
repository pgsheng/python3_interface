import wx  # 导入wxPython


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '用户登录', size=(400, 300))
        # 创建面板
        panel = wx.Panel(self)
        # 创建文本，左对齐
        self.title = wx.StaticText(panel, label="请输入用户名和密码")
        self.label_user = wx.StaticText(panel, label="用户名:")
        self.text_user = wx.TextCtrl(panel, style=wx.TE_LEFT)
        self.text_user.Bind(wx.EVT_TEXT,self.Input)
        self.label_pwd = wx.StaticText(panel, label="密   码:")
        self.text_password = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        # 创建“确定”和“取消”按钮, 并绑定事件
        self.bt_confirm = wx.Button(panel, label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel = wx.Button(panel, label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        # 添加容器，容器中控件按横向并排排列
        horizontal_user = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_user.Add(self.label_user, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL, border=5)
        horizontal_user.Add(self.text_user, proportion=1, flag=wx.ALL, border=5)

        horizontal_pwd = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_pwd.Add(self.label_pwd, proportion=0, flag=wx.ALIGN_CENTER_VERTICAL, border=5)
        horizontal_pwd.Add(self.text_password, proportion=1, flag=wx.ALL, border=5)

        horizontal_button = wx.BoxSizer(wx.HORIZONTAL)
        horizontal_button.Add(self.bt_confirm, proportion=0, flag=wx.ALIGN_CENTER, border=5)
        horizontal_button.Add(self.bt_cancel, proportion=1, flag=wx.ALIGN_CENTER, border=5)
        # 添加容器，容器中控件按纵向并排排列
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title, proportion=0, flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER,
                       border=15)
        vsizer_all.Add(horizontal_user, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(horizontal_pwd, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=45)
        vsizer_all.Add(horizontal_button, proportion=0, flag=wx.ALIGN_CENTER | wx.TOP, border=15)
        panel.SetSizer(vsizer_all)

    def OnclickSubmit(self, event):
        """ 点击确定按钮，执行方法 """
        message = ""
        username = self.text_user.GetValue()  # 获取输入的用户名
        password = self.text_password.GetValue()  # 获取输入的密码
        if username == "" or password == "":  # 判断用户名或密码是否为空
            message = '用户名或密码不能为空'
        elif username == 'admin' and password == '123456':  # 用户名和密码正确
            message = '登录成功'
        else:
            message = '用户名和密码不匹配'  # 用户名或密码错误
        wx.MessageBox(message)  # 弹出提示框

    def OnclickCancel(self, event):  # 没有event点击取消会报错
        """ 点击取消按钮，执行方法 """
        self.text_user.SetValue("")  # 清空输入的用户名
        self.text_password.SetValue("")  # 清空输入的密码

    def Input(self, event):  # 没有event点击取消会报错
        """ 点击取消按钮，执行方法 """
        username = self.text_user.GetValue()  # 获取输入的用户名
        print(username)

if __name__ == '__main__':
    app = wx.App()  # 初始化
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()  # 显示窗口
    app.MainLoop()  # 调用主循环方法
