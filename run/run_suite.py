import os
import sys



o_path = os.path.abspath(os.path.join(os.getcwd(), "./"))
sys.path.append(o_path)
import config
import unittest
# 路径都是相对路径 ->相对的是你的入口文件，执行文件
from tool.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover('script')
with open(config.BASE_PATH + '/report/mtx_shop.html', 'wb') as f:
    HTMLTestRunner(stream=f,title='码同学商场报告',description='码同学商城的登录用例的执行').run(suite)

# runner = unittest.TextTestRunner()
# runner.run(suite)