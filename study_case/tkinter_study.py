# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/13 22:09
"""
from tkinter import Tk, LEFT, RIGHT, mainloop, CENTER, Label

from PIL import ImageTk
from PIL import Image

def test1():
    root = Tk()
    # 创建一个文本Label对象
    textLabel = Label(root,  # 将内容绑定在  root 初始框上面
                      text="您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！",
                      justify=LEFT,  # 用于 指明文本的 位置
                      padx=10)  # 限制 文本的 位置 , padx 是 x轴的意思 .
    textLabel.pack(side=LEFT)  # 致命 textlabel 在初识框 中的位置

    # 创建一个图像Label对象
    img = Image.open(r"E:\PycharmProjects\python3_interface\study_case\data\a.png")
    photo = ImageTk.PhotoImage(img)
    imgLabel = Label(root, image=photo)  # 绑定在初始旷上面
    imgLabel.pack(side=RIGHT)  # 指明 图片位置

    mainloop()

def test2():
    root = Tk()

    img = Image.open(r"E:\PycharmProjects\python3_interface\study_case\data\a.png")
    photo = ImageTk.PhotoImage(img)
    theLabel = Label(root,
                     text="大家好,才是真的好.",  # 载入文本
                     justify=LEFT,  # 声明文本的位置
                     image=photo,  # 载入图片
                     compound=CENTER,  # 声明图片的位置
                     font=("楷体", 20),  # 声明文本字体
                     fg="black"  # 声明文本颜色 .
                     )
    theLabel.pack()  # 自动调整布局

    mainloop()


if __name__ == '__main__':
    test1()
    test2()
