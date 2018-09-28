# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/6/3 17:33
"""
import time

from selenium import webdriver

from public.log import Log


def test_webdriver():
    # log = Log("UI测试").get_logger()

    # driver = webdriver.Ie()
    driver = webdriver.Firefox()  # 获取浏览器驱动对象
    driver.set_window_size(960, 540)  # 设置窗口大小

    driver.get('https://www.baidu.com/')  # 打开一个网页
    # driver.find_element_by_id('kw').clear() # 清除文本
    """HTMl的属性定位,属性要唯一才能定位到"""
    # driver.find_element_by_id('kw').send_keys('王春玲') # 根据html属性id定位元素，模拟按键输入
    # driver.find_element_by_name('wd').send_keys('王春玲') # 根据html属性name定位元素，模拟按键输入
    # driver.find_element_by_class_name('s_ipt').send_keys('王春玲') # 根据html属性id定位元素，模拟按键输入
    # driver.find_element_by_tag_name('input').send_keys('王春玲') # 根据标签input定位，这里定位不到，因为页面有多个input
    # driver.find_element_by_link_text('贴吧').click() # 根据标签对之间的文本信息定位，如：<a>贴吧</a>
    # driver.find_element_by_partial_link_text('一个很长').click() # 根据标签对之间的部分文本信息定位，如：<a>一个很长很长的文本</a>
    """XPath定位"""
    # driver.find_element_by_xpath('/html/body/div/div/div[4]/div/div/from/span/input').send_keys('王春玲') # ，绝对路径定位
    # driver.find_element_by_xpath('//input[@id="kw"]').send_keys('王春玲') # XPath定位，根据元素属性id,还可以其他属性，//表示当前页面某目录
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys('王春玲') # XPath定位，根据元素属性，不指定标签名，用*替代
    # driver.find_element_by_xpath("//form[@id='form']/span/input").send_keys('王春玲') # XPath定位，上级和属性组合，
    # driver.find_element_by_xpath('//input[@id="kw" and @class="s_ipt"]').send_keys('王春玲') # 多个属性组合
    """CSS定位,属性要唯一才能定位到"""
    # driver.find_element_by_css_selector(".s_ipt").send_keys('王春玲') # css的class属性，注意：.代表class类型的
    # driver.find_element_by_css_selector("#kw").send_keys('王春玲') # css的id属性，注意：#代表id类型的
    # driver.find_element_by_css_selector("input").send_keys('王春玲') # 标签名定位，这里定位不到，不唯一
    driver.find_element_by_css_selector("span>input").send_keys('王春玲')  # 父子关系

    """
    显式等待和隐式等待:
    显式等待的等待时间是固定的，固定了10s就必须等待10s,隐式等待的等待时间是个范围，例如最大10s,那么如果在3s的
    时候程序达到预期的结果，那么就不在继续后面的7秒，直接进入下一步操作，而如果超出10s还没有相应，
    程序就会报出相应的错误。 
    """

    """
    implicitly_wait()隐式等待，用来设置超时，一般把implicitly_wait()方法调用在加载测试地址后，等待所测试的应用程序加载。
    如果 WebDriver没有在 DOM中找到元素，将继续等待，超出设定时间后则抛出找不到元素的异常。
    即当查找元素或元素并没有立即出现的时候，隐式等待将等待一段时间再查找 DOM，默认的时间是0
    一旦设置了隐式等待，则它存在整个 WebDriver 对象实例的声明周期中，隐式的等到会让一个正常响应的应用的测试变慢，
    它将会在寻找每个元素的时候都进行等待，这样会增加整个测试执行的时间。
    """
    # driver.implicitly_wait(30)

    # driver.find_element_by_id('kw').submit() # 提交输入框的内容,功能与click类似
    # driver.find_element_by_id('su').click() # 点击元素
    driver.find_element_by_xpath('//*[@id="su"]').click()  # 点击元素
    # size = driver.find_element_by_id('kw').size # 获取元素的大小
    # text = driver.find_element_by_id('cp').text # 获取元素的文本
    # attribute = driver.find_element_by_id('kw').get_attribute() # 获取元素的属性值
    # print(size)

    # driver.get_screenshot_as_file(Config.project_path + r'\test_data\a.png') # 截屏

    # time.sleep(3) #睡眠3秒
    # driver.back() # 返回上一个网页
    # time.sleep(3)
    # driver.refresh() # 刷新当前页面
    # driver.forward() # 前进

    # driver.maximize_window() # 设置窗口最大化
    # driver.minimize_window() # 设置窗口最小化

    time.sleep(5)
    # log.info(driver.title)  # 获取标题
    driver.execute_script("window.scrollTo(200,1000);")

    time.sleep(5)

    driver.quit()   # 退出浏览器
    # driver.close() # 关闭当前窗口


if __name__ == '__main__':
    test_webdriver()
