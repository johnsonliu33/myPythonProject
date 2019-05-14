# -*- coding:utf-8 -*-
import logging.config


def my_log():
    LOG_CONF = "../config/log.conf"
    logging.config.fileConfig(LOG_CONF)
    logger = logging.getLogger()
    return logger


if __name__ == '__main__':
    logger = my_log()
    logger.info("this is my log info")
    logger.error("this is my log error")
    logger.debug("this is my log debug")
