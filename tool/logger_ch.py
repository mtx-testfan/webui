'''
三大块
1.日志器  日志的入口，然后往里面写，比喻：日记本
级别越来越高（严重）  原则：你设置的级别，比他大的都会显示出来，比他低级的级别是不会显示出来的
debug（调试级别），info(信息级别)，warning（警告级别）,error(错误级别),critical(致命的，严重的)
2.格式器   以什么样的格式去写这个日志
3.处理器    表示对日志内容的一个处理方式，比如可以直接把日志输出到console里面，
或者是输出到文件里面
'''
# 导包：把日志模块和处理器都一并导入进来
import logging.handlers
# 获取日志器(日记本)
logger = logging.getLogger()
# 给日志器设置总的级别,级别是封装在logging里面的
# 我要设置错误级别,完全大写
logger.setLevel(logging.ERROR)
# 2.获取格式器
# 2.1这个只是要输出的样式
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
# 2.2 获取格式器 参数  具体要输出什么样的样式
fm = logging.Formatter(fmt)
# 3.获取处理器  按时间切割的文件处理器工作中用midnight  ,backupCount=3  除了原件，只保存最新的三个
tf = logging.handlers.TimedRotatingFileHandler(filename='../logger/test.log',
                                          when='H',
                                          interval=1,
                                          backupCount=3,
                                          encoding='utf-8')

# 在处理器中添加格式器
tf.setFormatter(fm)
# 给处理器设置一个级别
tf.setLevel(logging.INFO)
# 在日志器中添加处理器
logger.addHandler(tf)


if __name__ == '__main__':
    # 测试日志调用的时候
    logger.debug('调试')
    logger.info('信息')
    logger.warning('警告')
    logger.error('错误')
    logger.critical('致命的')