# -*- coding:utf-8 -*-
import datetime
import logging
import os
from logging import handlers

level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}  # 日志级别关系映射

level = 'debug'
when = 'D'
backCount = 3


dirPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
now_time = datetime.datetime.now().strftime("%Y-%m-%d")
filename = dirPath+"/logs/%s_log.log" % now_time
# print(filename)
logger = logging.getLogger(filename)
# 设置日志格式
fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
format_str = logging.Formatter(fmt)
format_str.datefmt = "%Y-%m-%d %H:%M:%S"
logger.setLevel(level_relations.get(level))  # 设置日志级别

console = logging.StreamHandler()  # 往屏幕上输出
console.setFormatter(format_str)  # 设置屏幕上显示的格式

# 往文件里写入
# 指定间隔时间自动生成文件的处理器
logfile = handlers.TimedRotatingFileHandler(filename=filename, when=when, interval=1, backupCount=backCount,
                                            encoding='utf-8')
# 实例化TimedRotatingFileHandler
# interval是时间间隔,单位是秒;
# backupCount是备份文件的个数，如果超过这个个数，就会自动删除;
# when是间隔的时间单位，单位有以下几种：
#   S 秒 ; M 分 ; H 小时 ; D 天 ; W 每星期（interval==0时代表星期一）; midnight 每天凌晨 ;
logfile.setFormatter(format_str)  # 设置文件里写入的格式

logger.addHandler(console)  # 把对象加到logger里
logger.addHandler(logfile)

if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')
