# -*- coding:utf-8 -*-
import os
import logging
import logging.config
from KeyWordAndDataDriver.config.varConfig import parentDirPath

# 读取日志配置文件
filename=os.path.join(parentDirPath, "config", "logger.conf")

logging.config.fileConfig(filename)
# 选择日志格式
logger = logging.getLogger("root")

if __name__ == '__main__':
    logger.debug('debug')
    logger.info('info')
    logger.warning('警告')
    logger.error('报错')
    logger.critical('严重')
