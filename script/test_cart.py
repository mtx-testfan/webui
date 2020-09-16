import time
import unittest
from page.page_login import PageLogin
from base1.driver import GetDriver
from page.page_cart import PageCart

'''
1.强相关性，不建议这样写，用例和用例之间，一定要有独立性，
有依赖性的话，一个用例失败了，是不是会影响另外一个用例的执行
这样不建议
2.不想让用例1和用例2有强依赖型，我们应该怎么做？
（1） 函数级别setup和teardown  实现不让用例之间有依赖性，
缺点：每次都得重新创建driver，销毁driver，效率低，耗时、
（2） 跳转到首页
'''


class TestCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver('chrome')
        # 调用登录成功的方法
        PageLogin(cls.driver).page_login_success()
        # 等待一会
        time.sleep(3)
        # 实例化购物车页面
        cls.cart = PageCart(cls.driver)



    def test_add_cart(self):
        # try...except..捕获异常 目的：为了截图,截图之后把错误信息抛出去
        self.cart.page_add('雪纺连衣裙')
        self.assertIn('加入成功', self.cart.base_page_source)

    # 每一个函数执行完之后都会执行一次
    def tearDown(self) -> None:
        # 点击首页
        self.cart.base_click_index()




    # 用例2
    def test_delete(self):
        # 调用删除方法
        self.cart.page_delete()
        time.sleep(3)
        # 断言
        self.assertFalse(self.cart.page_if_delete_button_exist())

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().close_driver()


