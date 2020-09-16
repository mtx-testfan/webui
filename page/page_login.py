import time
from base1.base import Base
import page


class PageLogin(Base):
    # 点击登录链接前缀page 页面层 见名知意  loc元素定位的东西
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_input_username, username)

    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_input_password, password)

    # 点击登录  修改超时时间和频率
    def page_click_login_button(self):
        self.base_click(page.login_click_login_button )

    # todo  检查点 通过判断页面上是否有登录链接这个按钮来判断是否登录成功
    # 因为你要用这个值做断言，所以return  返回这个值
    def page_el_if_is_exist(self):
        time.sleep(5)
        return self.base_if_is_exist(page.login_link)

    # 组合业务逻辑->跟你做功能测试一样的一个组合的动作，动作顺序一样
    def page_login(self, username, password):
        # 点击登录链接
        self.page_click_login_link()
        # 输入用户名
        self.page_input_username(username)
        # 输入密码
        self.page_input_password(password)
        # 点击登录
        self.page_click_login_button()
    # 正确登录的业务(为了方便其他功能使用)
    def page_login_success(self):
        # 点击登录链接
        self.page_click_login_link()
        # 输入用户名
        self.page_input_username('yaoyao')
        # 输入密码
        self.page_input_password('yaoyao')
        # 点击登录
        self.page_click_login_button()

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://121.42.15.146:9090/mtx/')
    login = PageLogin(driver)
    login.page_login('yaoyao','yaoyao')
    # print(login.page_el_if_is_exist())
    assert login.page_el_if_is_exist() == False
