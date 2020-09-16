'''
封装一些基础操作方法，你经常用的
'''
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tool.logger import GetLooger
# 获取日志的一个入口
log = GetLooger().get_logger()

class Base:
    def __init__(self, driver):
        '''原则：调试，print一样，代码的一个解释'''
        log.info('正在初始化获取driver对象:{}'.format(driver))
        self.driver = driver

    # 找元素(加等待,显性等待) 缺省参数 在定义的函数的时候有默认参数
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        log.info("正在查找元素：{}元素,最多等待: {}秒".format(loc, timeout))
        # 显性等待
        el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
        return el

    # 点击
    def base_click(self, loc):
        log.info('正在点击:{}元素'.format(loc))
        self.base_find_element(loc).click()

    # 输入(清空，输入)
    def base_input(self, loc, value):
        log.info('正在输入：{}元素 输入值是: {}'.format(loc,value))
        # 获取元素
        el = self.base_find_element(loc)
        # 先清空
        el.clear()
        # 在输入
        el.send_keys(value)

    # 获取文本内容
    def base_get_text(self,loc):
        log.info(f'定位到元素{loc}')
        return self.base_find_element(loc).text

    # 切换window
    def base_switch_window(self,title):
        for handle in self.driver.window_handles:
            log.info('开始切换窗口')
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                log.info('窗口切换成功')
                break

    # 切换iframe
    def base_switch_iframe(self,frame):
        self.driver.switch_to.frame(frame)

    # 切回默认的iframe
    def base_default_iframe(self):
        self.driver.switch_to.default_content()

    # 截图操作
    def base_get_image(self):
        log.info('开始截图====')
        self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y-%m-%d_%H_%M_%S')))

    # 添加cookie
    def base_add_cookie(self,name,value):
        '''
        添加cookie
        :param name:
        :param value:
        :return:
        '''
        log.info('正在添加cookie=====')
        self.driver.add_cookie({'name': name, 'value': value})

    # 判断元素是否存在
    def base_if_is_exist(self,loc):
        '''
        如果可以找到元素，那么就返回True，找不到就返回False
        :param loc:
        :return:
        '''
        try:
            log.info(f'判断{loc}元素是否存在')
            self.base_find_element(loc)
            log.info(f'{loc}元素是存在的')
            return True
        except:
            log.error(f'{loc}元素不存在')
            return False

    # 进入首页
    def base_click_index(self):
        loc = By.XPATH, '//*[@id="doc-topbar-collapse"]/ul/li[1]/a'
        self.base_click(loc)
        log.info('点击回到首页')

    # @property 加上这个就会把函数变成属性-前提是你的函数是不需要传参数的
    @property
    def base_page_source(self):
        return self.driver.page_source

    def base_js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.base_js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)
        log.info("Execute JavaScript scripts. %s" % script)

    def base_max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.base_max_window()
        '''
        self.driver.maximize_window()
        log.info("Set browser window maximized")

    def base_set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.base_set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)
        log.info(" Set browser window %s wide and  %s high." % (wide, high))

    def base_get_attribute(self,loc, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.base_get_attribute(By.CLASS_NAME, 'btn-go',"value")
        '''
        el = self.base_find_element(loc)
        log.info("Gets the value %s of an element attribute %s" % (attribute, loc))
        return el.get_attribute(attribute)

    def base_get_display(self, loc):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.base_get_display(By.CLASS_NAME, 'btn-go')
        '''
        el = self.base_find_element(loc)
        log.info("The %s element is exits or not" % loc)
        return el.is_displayed()

    def base_get_title(self):
        '''
        Get window title.

        Usage:
        driver.base_get_title()
        '''
        log.info("Get window title.")
        return self.driver.title

    def base_select(self, loc, value):
        '''
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against

        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.base_select("#nr", '20')
            loc = By.CLASS_NAME, 'btn-go'
            driver.base_select(By.CLASS_NAME, 'btn-go', '20')
        '''
        # 先找到元素
        el = self.base_find_element(loc)
        #实例化下拉框，获取select下拉框里面option的值
        Select(el).select_by_value(value)

    def base_forward(self):
        self.driver.forward()
        log.info("Click forward on current page.")

    def base_back(self):
        self.driver.back()
        log.info("Click back on current page.")

    def base_get_alert_text(self):
        '''
        Gets the text of the Alert.

        Usage:
        driver.base_get_alert_text()
        '''
        log.info("Gets the text of the Alert.")
        return self.driver.switch_to.alert.text

    def base_implicitly_wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.base_implicitly_wait(10)
        '''
        self.driver.implicitly_wait(secs)
        log.info("wait for %d seconds." % secs)

    def base_accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.base_accept_alert()
        '''
        self.driver.switch_to.alert.accept()
        log.info("Accept warning box.")

    def base_dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.base_dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()
        log.info("Dismisses the alert available.")


if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.get('http://121.42.15.146:9090/mtx/')
    base = Base(driver)
    base.base_add_cookie('PHPSESSID','prdk5cbchgl6pavdofr9qs4b92')
    driver.refresh()

