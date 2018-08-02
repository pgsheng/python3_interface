# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/6/3 17:33
"""
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from public import config
from public.log import Log


class BasePage(object):
    """
        定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, url):
        self.log = Log().get_logger()
        self.url = url
        # 启动浏览器
        # self.driver = webdriver.Ie()
        # self.driver = webdriver.Edge()
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        # driver.implicitly_wait(5)  # 隐式等待

    def get_driver(self):
        return self.driver

    def max_window(self):
        self.driver.maximize_window()

    def set_window(self, wide, high):
        self.driver.set_window_size(wide, high)

    # 退出浏览器
    def quit(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()

    # 浏览器后退操作
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            self.log.error("Failed to quit the browser with %s" % e)

    # 获取当前网页的标题
    def get_title(self):
        return self.driver.title

    # 获取当前网页的url
    def get_url(self):
        return self.driver.current_url

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    # 清除文本框
    def clear(self, selector):
        try:
            el = self.element_wait(selector)
            el.clear()
        except Exception as e:
            self.log.error("Failed to clear in input box with %s" % e)
            self.take_screenshot('clear_failure')

    # 直接输入
    def type(self, css, text):
        try:
            el = self.element_wait(css)
            el.send_keys(text)
        except Exception as e:
            self.log.error("Failed to type in input box with %s" % e)
            self.take_screenshot('input_box_failure')
            raise

    # 清空并输入
    def clear_type(self, css, text):
        try:
            el = self.element_wait(css)
            el.clear()
            el.send_keys(text)
        except Exception as e:
            self.log.error("Failed to type in input box with %s" % e)
            self.take_screenshot('input_box_failure')
            raise

    # 点击元素
    def click(self, selector):
        try:
            el = self.element_wait(selector)
            el.click()
        except Exception as e:
            self.log.error("Failed to click the element with %s" % e)
            self.take_screenshot('click_failure')
            raise

    # 右键
    def right_click(self, css):
        try:
            el = self.element_wait(css)
            ActionChains(self.driver).context_click(el).perform()
        except Exception as e:
            self.log.error("Failed to click the element with %s" % e)
            self.take_screenshot('right_click_failure')
            raise

    # 双击
    def double_click(self, css):
        try:
            el = self.element_wait(css)
            ActionChains(self.driver).double_click(el).perform()
        except Exception as e:
            self.log.error("Failed to click the element with %s" % e)
            self.take_screenshot('double_click_failure')
            raise

    # 鼠标移到指定元素上
    def move_to_element(self, css):
        try:
            el = self.element_wait(css)
            ActionChains(self.driver).move_to_element(el).perform()
        except Exception as e:
            self.log.error("Failed to move to the element with %s" % e)
            self.take_screenshot('move_to_failure')
            raise

    # 拖拽到某个元素然后松开
    def drag_and_drop(self, el_css, ta_css):
        try:
            element = self.element_wait(el_css)
            target = self.element_wait(ta_css)
            ActionChains(self.driver).drag_and_drop(element, target).perform()
        except Exception as e:
            self.log.error("Failed to drag_and_drop with %s" % e)
            self.take_screenshot('drag_and_drop_failure')
            raise

    #  Submit the specified form.
    def submit(self, css):
        try:
            el = self.element_wait(css)
            el.submit()
        except Exception as e:
            self.log.error("Failed to submit with %s" % e)
            self.take_screenshot('submit_failure')
            raise

    # f5 刷新
    def F5(self):
        self.driver.refresh()

    def js(self, script):
        """
        Usage: driver.js("window.scrollTo(200,1000);")
        """
        try:
            self.driver.execute_script(script)
        except Exception as e:
            self.log.error("Failed to js with %s" % e)
            self.take_screenshot('js_failure')
            raise

    # 获取元素的属性
    def get_attribute(self, css, attribute):
        try:
            el = self.element_wait(css)
            return el.get_attribute(attribute)
        except Exception as e:
            self.log.error("Failed to get_attribute with %s" % e)
            self.take_screenshot('get_attribute_failure')
            raise

    # 获取元素的文本信息
    def get_text(self, css):
        try:
            return self.element_wait(css).text
        except Exception as e:
            self.log.error("Failed to get_text with %s" % e)
            self.take_screenshot('get_text_failure')
            raise

    # 切换到指定的警告弹窗口并点击确认
    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    # 切换到指定的警告弹窗口并点击取消
    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    # 切换到指定的帧视图
    def switch_to_frame(self, css):
        try:
            iframe_el = self.element_wait(css)
            self.driver.switch_to.frame(iframe_el)
        except Exception as e:
            self.log.error("Failed to switch_to_frame with %s" % e)
            self.take_screenshot('switch_to_frame_failure')
            raise

    # 退出当前的帧视图
    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()

    # 打开并切换到新窗口
    def open_new_window(self, css):
        try:
            original_windows = self.driver.current_window_handle
            self.element_wait(css).click() # 点击元素打开新窗口
            all_handles = self.driver.window_handles
            for handle in all_handles:
                if handle != original_windows:
                    self.driver.switch_to.window(handle) # 切换到新窗口
        except Exception as e:
            self.log.error("Failed to open_new_window with %s" % e)
            self.take_screenshot('open_new_window_failure')
            raise

    # 判断元素是否存在
    def element_exist(self, css):
        try:
            self.element_wait(css)
            return True
        except TimeoutException:
            return False

    # 保存图片
    def take_screenshot(self, name):
        now_time = time.strftime('%Y%m%d') + '_'
        screen_name = config.test_screenshot_path + now_time + name + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except Exception as e:
            self.log.error("Failed to take screenshot! %s" % e)
            raise

    def type_and_enter(self, css, text, secs=0.5):
        """
        Operation input box. 1、input message,sleep 0.5s;2、input ENTER.
        """
        try:
            ele = self.element_wait(css)
            ele.send_keys(text)
            time.sleep(secs)
            ele.send_keys(Keys.ENTER)
        except Exception as e:
            self.log.error("Failed to type_and_enter with %s" % e)
            self.take_screenshot('type_and_enter_failure')
            raise

    def js_click(self, css):
        try:
            js_str = "$('{0}').click()".format(css)
            self.driver.execute_script(js_str)
        except Exception as e:
            self.log.error("Failed to js_click with %s" % e)
            self.take_screenshot('js_click_failure')
            raise

    # 定位元素方法
    def get_element(self, css):
        """
         根据=>来切割字符串
        """
        if '=>' not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split('=>')[0]
        value = css.split('=>')[1]

        if by == "i" or by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == "n" or by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == "c" or by == 'class':
            element = self.driver.find_element_by_class_name(value)
        elif by == "l" or by == 'link_text':
            element = self.driver.find_element_by_link_text(value)
        elif by == "p" or by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(value)
        elif by == "x" or by == 'xpath':
            element = self.driver.find_element_by_xpath(value)
        elif by == "s" or by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError(
                "elements must is,'id','name','class','link_text','partial_link_text',xpaht','css'.")
        return element

    # 显式等待
    def element_wait(self, css, secs=5):
        """
        等待元素显示
        Usage:
        driver.element_wait("id->kw",10)
        """
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0].strip()
        value = css.split("=>")[1].strip()
        messages = 'Element: {0} not found in {1} seconds.'.format(css, secs)

        if by == "i" or by == 'id':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)), messages)
        elif by == "n" or by == 'name':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)),messages)
        elif by == "c" or by == 'class':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)),messages)
        elif by == "l" or by == 'link_text':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)),messages)
        elif by == "p" or by == 'partial_link_text':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)), messages)
        elif by == "x" or by == 'xpath':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)),messages)
        elif by == "s" or by == 'css':
            element = WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)), messages)
        else:
            raise NameError(
                "elements must is,'id','name','class','link_text','partial_link_text','xpaht','css'.")
        return element
