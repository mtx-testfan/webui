# 三.业务逻辑层--->就相当于最终的调用层，需要给底层传各种参数，
# 他就调用组合好的业务，实现业务逻辑。
import time
import unittest
from base1.driver import GetDriver
from page.page_login import PageLogin
from base1.openDriver import OpenDriver
import page
import ddt
# 获取日志的一个入口
from tool.logger import GetLooger

log = GetLooger().get_logger()
# 逆向数据 data->列表套字典  (文件 excel，txt，yaml)
# data = [
#         {'username': 'yaoyao', 'password': 'yaoyao1'},
#         {'username': 'beihe', 'password': 'beihe'},
#         {'username': 'yaoyao1', 'password': 'yaoyao6'},
#
#         ]
from tool.readExcel2 import ReadExcel

data = ReadExcel().get_excel(['username','password'])
# 作业 data = 列表套列表 然后做参数化

@ddt.ddt
class Login(unittest.TestCase):
    # 类属性->全局再类方法和实例方法去用，都可以
    driver = None
    login = None

    # 前置函数->打开浏览器，实例化page对象：准备工作
    @classmethod
    def setUpClass(cls):
        # 打开浏览器 driver 局部变量
        cls.driver = GetDriver().get_driver('chrome')
        cls.login = PageLogin(cls.driver)


    # 后置函数->关闭浏览器：清理工作
    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().close_driver()
    # 业务的测试用例->测试业务是否正常登录，输入具体的跟业务有关的参数，还有做断言

    @ddt.data(*data)
    def test_login(self, data):
        # data-》字典
        # 调用登录业务
        self.login.page_login(data['username'], data['password'])
        #  调用进行断言的方法 断言 登录链接那个按钮是否存在  登录失败（错误账号）-return true
        #  登录成功（账号正确）->return false

        # result = self.login.page_el_if_is_exist()
        # time.sleep(5)
        # log.info(f'result的值是{result}')
        # 断言
        self.assertEqual(self.driver.title,'用户登录 - 码同学实战系统')

