# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/7/27 11:28
"""
import subprocess
import time
from appium import webdriver

class MyAppium(object):

    def test_calculator(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '5.1.1'  # Android系统版本
        desired_caps['deviceName'] = '192.168.253.101:5555'  # 模拟器名称，可以使用adb devices命令查看
        desired_caps['appPackage'] = 'com.android.calculator2'  # APP包名
        desired_caps['appActivity'] = '.Calculator'  # 要测试的APP的页面（即要打开的activity）

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        driver.find_element_by_name("1").click()
        driver.find_element_by_name("5").click()
        driver.find_element_by_name("删除").click()
        driver.find_element_by_name("5").click()
        driver.find_element_by_name("+").click()
        driver.find_element_by_name("6").click()
        driver.find_element_by_name("=").click()

        time.sleep(2)
        driver.quit()


    def test_cloud_call(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 平台
        desired_caps['platformVersion'] = '5.1.1'  # Android系统版本
        desired_caps['deviceName'] = '192.168.253.101:5555'  # 模拟器名称，可以使用adb devices命令查看
        desired_caps['appPackage'] = 'com.besttone.ccdt'  # APP包名
        desired_caps['noReset'] = True
        desired_caps['appActivity'] = 'com.besttone.ccdt.options.main.MainDrawerActivity'  # 要测试的APP的页面（即要打开的activity）

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # driver.find_element_by_name("已拨号码").click()
        driver.find_element_by_name("客户").click()

        time.sleep(5)
        driver.quit()


if __name__ == '__main__':
    n = MyAppium()
    # test_calculator()
    n.test_cloud_call()
