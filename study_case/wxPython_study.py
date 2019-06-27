import wx  # 导入wxPython


class App(wx.App):
    def OnInit(self):  # 初始化方法
        frame = wx.Frame(parent=None, id=-1, title='程序', pos=(200, 200), size=(300, 300))  # 创建顶级窗口

        panel = wx.Panel(self)  # 创建画板
        # 创建标题，并设置字体
        title = wx.StaticText(panel, label='Python之禅——Tim Peters', pos=(100, 20))
        font = wx.Font(16, wx.DEFAULT, wx.FONTSTYLE_NORMAL, wx.NORMAL)
        title.SetFont(font)
        # 创建文本
        wx.StaticText(panel, label='优美胜于丑陋', pos=(50, 50))
        wx.StaticText(panel, label='明了胜于晦涩', pos=(50, 70))
        wx.StaticText(panel, label='简洁胜于复杂', pos=(50, 90))
        wx.StaticText(panel, label='复杂胜于凌乱', pos=(50, 110))
        wx.StaticText(panel, label='扁平胜于嵌套', pos=(50, 130))
        wx.StaticText(panel, label='间隔胜于紧凑', pos=(50, 150))
        wx.StaticText(panel, label='可读性很重要', pos=(50, 170))
        wx.StaticText(panel, label='即便假借特例的实用性之名，也不可违背这些规则', pos=(50, 190))
        wx.StaticText(panel, label='不要包容所有错误，除非你确定需要这样做', pos=(50, 210))
        wx.StaticText(panel, label='当存在多种可能，不要尝试去猜测', pos=(50, 230))
        wx.StaticText(panel, label='而是尽量找一种，最好是唯一一种明显的解决方案', pos=(50, 250))
        wx.StaticText(panel, label='虽然这并不容易，因为你不是 Python 之父', pos=(50, 270))
        wx.StaticText(panel, label='做也许好过不做，但不假思索就动手还不如不做', pos=(50, 290))
        wx.StaticText(panel, label='如果你无法向人描述你的方案，那肯定不是一个好方案;反之亦然', pos=(50, 310))
        wx.StaticText(panel, label='命名空间是一种绝妙的理念，我们应当多加利用', pos=(50, 330))


        frame.Show()  # 显示窗口
        return True  # 返回值(返回窗口，在屏幕展示)



if __name__ == '__main__':
    app = App()  # 实例化App类
    app.MainLoop()  # 调用App类的MainLoop()主循环方法

'''
wx.Frame(parent=None, id=-1, title="", pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DfEFAULT_DIALOG_STYLE, name="frame")

parent：框架的父窗口。如果是顶级窗口，这个值是None
id：关于新窗口的wxPython ID号。通常设为-1，让wxPython自动生成一个新的ID
title：窗口标题
pos：wx.Point对象，指定左上角在屏幕位置。这个默认值(-1,-1)将让系统决定窗口的位置
size：一个wx.Python对象，指定这个窗口的初始尺寸，这个默认值(-1,-1)将让系统决定窗口的初始尺寸
style：指定窗口的类型的常量。可以使用或运算来组合他们。
name：框架内在的名字。可以使用它来寻找这个窗口
'''
