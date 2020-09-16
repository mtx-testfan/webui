import unittest
# 路径都是相对路径 ->相对的是你的入口文件，执行文件
from script.test_login import Login
from tool.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('script')

with open('../report/mtx_shop.html', 'wb') as f:
    HTMLTestRunner(stream=f,title='码同学商场报告',description='码同学商城的登录用例的执行').run(suite)

