# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/6/3 17:33
"""
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

from public.log import Log


def test_alert():
    log = Log("UI测试").get_logger()
    driver = webdriver.Firefox()
    driver.set_window_size(960, 540)  # 设置窗口大小
    driver.get('http://sahitest.com/demo/promptTest.htm')

    time.sleep(2)
    driver.find_element_by_name('b1').click()

    # a1 = driver.switch_to.alert  # 通过switch_to.alert切换到alert
    a1 = Alert(driver)  # 直接实例化Alert对象
    time.sleep(2)
    log.info(a1.text)  # 获取alert文本内容，对有信息显示的alert框

    a1.send_keys('send some words to alert!')  # 往prompt型alert中传入字符串
    time.sleep(2)
    a1.accept()  # 等同于点击“确认”或“OK”
    # a1.dismiss() # 等同于点击“取消”或“Cancel”
    log.info(driver.find_element_by_name('t1').get_attribute('value'))

    driver.quit()


def test_window():
    log = Log("UI测试").get_logger()
    driver = webdriver.Firefox()
    driver.set_window_size(960, 540)  # 设置窗口大小
    driver.get('http://sahitest.com/demo/index.htm')

    time.sleep(2)

    current_window = driver.current_window_handle  # 获取当前窗口的handle name
    time.sleep(5)
    driver.find_element_by_link_text('Window Open Test With Title').click()  # 新窗口打开另一个网页
    # driver.find_element_by_link_text('Window Open Test').click()  # 新窗口打开另一个网页

    time.sleep(2)
    all_windows = driver.window_handles  # 获取所有窗口handle name
    # 切换window，如果window不是当前window，则切换到该window
    for window in all_windows:
        if window != current_window:
            driver.switch_to.window(window)  # 只能通过window的handle name来切换窗口

    """
    如果打开多个浏览器句柄和标签页的对应关系：
    标签页顺序（按照打开顺序）：1,2,3,4,5
    对应的句柄   ：0,4,3,2,1
    """
    # driver.switch_to.window(driver.window_handles[2])

    log.info(driver.title)  # 打印当前页面title

    driver.close()
    time.sleep(5)
    driver.switch_to.window(current_window)  # 关闭新窗口之后，driver并不会自动跳转回原窗口，而是需要你switch回来
    log.info(driver.title)  # 打印原页面title

    driver.quit()


def test_frame():
    log = Log("UI测试").get_logger()
    driver = webdriver.Ie()
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    driver.set_window_size(1100, 600)  # 设置窗口大小
    # driver.maximize_window()

    """
    163邮箱登录的例子来用新的switch_to方法写一下，并通过观察，
    我们发现进入这个页面后焦点直接就定位到输入框里了，所以我们可以通过active_element()来定位。
    """
    # 进入163邮箱首页
    driver.get("http://mail.163.com/")
    time.sleep(2)
    # 切换到包含登录框的frame下
    driver.switch_to.frame("x-URS-iframe")  # 根据frame的id切换到frame
    # driver.switch_to.parent_frame() # 可以切换到上一层的frame，对于层层嵌套的frame很有用
    time.sleep(2)

    # 通过定位输当前焦点元素，并再次输入数据
    driver.switch_to.active_element.send_keys("123")
    # driver.find_element_by_css_selector('form>div>div>div>input').send_keys("123")
    log.info(driver.title)  # 打印原页面title

    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    # test_alert()
    test_window()
    # test_frame()
