import wx  # 导入wxPython


class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title="创建StaticText类",
                           pos=(200, 200), size=(400, 400))

        panel = wx.Panel(self)  # 创建画板，将panel 作为父类，然后将组件放入窗体中

        # 创建文本和输入框
        self.title = wx.StaticText(panel, label="请输入用户名和密码", pos=(140, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        self.title.SetFont(font)  # 设置字体
        self.label_user = wx.StaticText(panel, label="用户名:", pos=(50, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT,value='请输入用户名')
        # print(self.text_user)
        self.label_pwd = wx.StaticText(panel, pos=(50, 90), label="密   码:")
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)
        # print(self.text_password)


if __name__ == '__main__':
    app = wx.App()                      # 初始化应用
    frame = MyFrame(parent=None, id=-1)  # 实例MyFrame类，并传递参数
    frame.Show()                        # 显示窗口
    app.MainLoop()                      # 调用主循环方法

'''
一、wx.Frame(parent=None, id=-1, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DfEFAULT_DIALOG_STYLE, name="frame")

parent：框架的父窗口。如果是顶级窗口，这个值是None
id：关于新窗口的wxPython ID号。通常设为-1，让wxPython自动生成一个新的ID
title：窗口标题
pos：wx.Point对象，指定左上角在屏幕位置。这个默认值(-1,-1)将让系统决定窗口的位置
size：一个wx.Python对象，指定这个窗口的初始尺寸，这个默认值(-1,-1)将让系统决定窗口的初始尺寸
style：指定窗口的类型的常量。可以使用或运算来组合他们。
name：框架内在的名字。可以使用它来寻找这个窗口

二、wx.TextCtrl(parent, id, value="", pos=wx.DefaultPosition, size=wx.DefaultSize,style=0,validator=wx.DefaultValidator name=wx.TextCtrlNameStr)
style：单行wx.TextCtrl的样式，取值如下：
        wx.TE_CENTER：控件中的文本居中
        wx.TE_LEFT：控件中的文本左对齐
        wx.TE_NOHIDESEL：文本始终高亮显示，仅适用于Windows
        wx.TE_PASSWORD：不显示所键入的文本，以（*）代替显示
        wx.TE_PROCESS_ENTER：如果使用改参数，那么当用户在控件内按下Enter键时，一个文本输入事件将被触发。否则，按键事件由该文本控件或该对话框管理
        wx.TE_PROCESS_TAB：如果指定了这个样式，那么通常的字符事件在按下Tab键时创建（一般意味着一个制表符将被插入文本）。否则，tab由对话框来管理，通常是控件间切换
        wx.TE_READONLY：文本控件为只读，用户不能修改其中文本
        wx.TE_RIGHT：控件中的文本右对齐
value：显示在该控件中的初始文本
validator：常用于过滤数据以确保只能键入要接受的数据
'''
