import os
import sys
#
import page
# import page.setting
from base1.openDriver import OpenDriver
class GetDriver:
    # 获取driver，这个浏览器没有打开，标记判断的标记
    driver = None
    @classmethod
    def get_driver(cls,browser):
        if cls.driver is None:
            cls.driver = OpenDriver().get_driver(browser)
            cls.driver.maximize_window()
            # cls.driver.get(page.url)
            cls.driver.get(page.url)
            return cls.driver

    # 关闭driver
    @classmethod
    def close_driver(cls):
        # 为了程序的健壮性，需要先判断不为空的时候再执行
        if cls.driver:
            cls.driver.quit()
            # 必须 置空
            cls.driver = None


if __name__ == '__main__':
    GetDriver().get_driver('chrome')
    GetDriver().get_driver('chrome')