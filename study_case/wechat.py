# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/8/31 17:32
"""

import time

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:5555',
    'platformVersion': '5.1.1',
    'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
# 打开微信后等待5s时间
num = 0
num0 = 0
while 1:
    driver.find_element_by_id("com.tencent.mm:id/an7").click()
    # 点开最顶端的群聊
    try:
        driver.find_element_by_id("com.tencent.mm:id/a92").click()
        # 如果有多条消息未读按钮，则点击以到达未读消息顶端
    except:
        while num0 < 5:
            if num < 5:
                try:
                    driver.find_element_by_id("com.tencent.mm:id/abz").click()
                    # 如果找到红包，则打开
                except:
                    driver.swipe(300, 1000, 300, 300, 0)
                    num0 += 1
                    # 没有找到红包，则向上大幅度划动一次，num0+1
                try:
                    driver.find_element_by_id("com.tencent.mm:id/bv8").click()
                    # 如果打开了红包，则点击“开”
                except:
                    num += 1
                    # 如果五次打不开红包，则认为此群的没有可以继续打开的红包，退出群聊
                try:
                    driver.find_element_by_id("com.tencent.mm:id/hg").click()
                    # 领取完红包之后，点击左上角的箭头以返回
                except:
                    pass
                try:
                    driver.find_element_by_id("com.tencent.mm:id/bsv").click()
                    # 如果红包未领取完已过期，则点击×返回
                except:
                    pass
                driver.swipe(100, 450, 100, 200, 0)
                # 向下滑动以找到下一个红包的位置
            else:
                break
        try:
            driver.find_element_by_id("android:id/text1").click()
            # 执行完毕，退出群聊
        except:
            driver.find_element_by_id("com.tencent.mm:id/h1").click()
            # 如果点开了公众号列表，则点击左上角退出
    num = 0
    num0 = 0
    time.sleep(1)
    driver.swipe(100, 400, 100, 200, 0)
    # 找到下一个群聊的位置
