'''
封装具体你要打开哪一个浏览器，然后获取哪一个浏览器的driver
'''
from selenium import webdriver
# try:
#     print1(11)
# except Exception as e:
#     print(e)
#     # 主要为了中间做点啥
#     # 把错误抛出
#     raise


class OpenDriver(object):
    def driver(self,browser="chrome"):
        '''
        (可写可不写)
        好处： 功能分明，然后查看起来比较方便
        主要是返回封装好的driver
        :return:
        '''
        driver = self.get_driver(browser=browser)
        return driver


    def get_driver(self, browser):
        '''
        具体的浏览器driver的封装过程

        :param browser:
        :return:
        '''
        if browser == 'firefox' or browser =='ff':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'chrome' or browser == 'ch':
            # driver = webdriver.Chrome(R"D:\chromedriver.exe")
            return webdriver.Chrome(r'../tool/chromedriver.exe')
        elif browser == 'ie' or browser == 'internet explorer':
            return webdriver.Ie()
        elif browser == '360':
            return webdriver.Ie()
        else:
            raise NameError('Not found %s browser,you must input "firefox","ff","chrome","ie"'% browser)


if __name__ == '__main__':
    Op = OpenDriver()
    driver = Op.driver("ie")