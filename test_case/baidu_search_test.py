# coding=utf-8
import time
import unittest
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.homepage = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.homepage.quit()

    # def test_aclick_news(self):
    #     self.homepage.click_news()  # 调用页面对象类中的点击搜索按钮方法
    #     self.homepage.sleep(2)
    #     self.homepage.get_screenshot_img('click_news')  # 调用基类截图方法
    #     self.homepage.sleep(2)
    #     self.homepage.back()

    def test_baidu_search(self):
        self.homepage.sleep(2)
        self.homepage.search_input('selenium')  # 调用页面对象中的方法
        self.homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.homepage.sleep(2)
        self.homepage.get_screenshot_img('selenium')  # 调用基类截图方法
        self.homepage.sleep(2)
        self.homepage.back()
        try:
            assert 'selenium' in self.homepage.get_title()  # 调用页面对象继承基类中的获取页面标题方法
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_baidu_search2(self):
        self.homepage.sleep(2)
        self.homepage.search_input('python')  # 调用页面对象中的方法
        self.homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.homepage.sleep(2)
        self.homepage.get_screenshot_img('python')  # 调用基类截图方法

if __name__ == '__main__':
    unittest.main()