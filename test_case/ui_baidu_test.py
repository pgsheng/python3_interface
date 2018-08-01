# coding=utf-8
import unittest
from pageobjects.baidu_homepage import HomePage
from public.log import Log


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

    def test_baidu_search(self):
        self.home_page.sleep(2)
        self.home_page.search_input('selenium')  # 调用页面对象中的方法
        self.home_page.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.home_page.sleep(2)
        self.home_page.get_screenshot_img('selenium')  # 调用基类截图方法
        self.home_page.sleep(2)
        self.home_page.back()
        try:
            assert 'selenium' in self.home_page.get_title()  # 调用页面对象继承基类中的获取页面标题方法
            self.log.info('Test Pass.')
        except Exception as e:
            self.log.info('Test Fail.', format(e))

    def test_baidu_search2(self):
        self.home_page.sleep(2)
        self.home_page.search_input('python')  # 调用页面对象中的方法
        self.home_page.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        self.home_page.sleep(2)
        self.home_page.get_screenshot_img('python')  # 调用基类截图方法

    @classmethod
    def tearDownClass(self):
        self.home_page.quit()


if __name__ == '__main__':
    unittest.main()
