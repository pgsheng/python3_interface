# coding=utf-8
import unittest

from ddt import ddt, data

from pageobjects.baidu_homepage import HomePage
from public import base
from public.log import Log

testdata = base.get_excel_data('test.xlsx', 'test2')

@ddt
class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.log = Log('测试').get_logger()
        cls.home_page = HomePage()

    # def test_aclick_news(self):
    #     self.homepage.click_news()  # 调用页面对象类中的点击搜索按钮方法
    #     self.homepage.sleep(2)
    #     self.homepage.get_screenshot_img('click_news')  # 调用基类截图方法
    #     self.homepage.sleep(2)
    #     self.homepage.back()

    @data(*testdata)
    def test_1baidu_search(self,data):
        self.home_page.sleep(1)
        self.home_page.search_input(data.get("name"))  # 调用页面对象中的方法
        self.home_page.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.home_page.sleep(1)
        self.home_page.take_screenshot(data.get("name"))  # 调用基类截图方法
        self.home_page.back()
        self.assertIn(data.get("name"), self.home_page.get_title(), msg='和预期不一样')

    def test_2baidu_search(self):
        self.home_page.sleep(1)
        self.home_page.search_input('python')  # 调用页面对象中的方法
        self.home_page.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.home_page.sleep(1)
        self.home_page.take_screenshot('python')  # 调用基类截图方法
        self.assertIn("python", self.home_page.get_title(), msg='和预期不一样')

    @classmethod
    def tearDownClass(self):
        self.home_page.quit()


if __name__ == '__main__':
    unittest.main()