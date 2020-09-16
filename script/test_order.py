import time
import unittest
from base1.driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder

class Order(unittest.TestCase):
    driver = None
    order = None
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化driver
        cls.driver = GetDriver().get_driver('chrome')
        # 调用成功登陆的方法
        PageLogin(cls.driver).page_login_success()
        time.sleep(3)
        # 实例化order的page页面
        cls.order = PageOrder(cls.driver)


    @classmethod
    def tearDownClass(cls) -> None:
        # 销毁，善后操作-关闭浏览器
        GetDriver().close_driver()

    def test_order(self):
        try:
            self.order.page_order()
            time.sleep(3)
            self.assertIn('支付成功', self.order.base_page_source)
        except Exception as e:
            self.order.base_get_image()
            raise e


if __name__ == '__main__':
    unittest.main()