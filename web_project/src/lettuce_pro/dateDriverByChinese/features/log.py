# -*- coding:utf-8 -*-
import logging
# 初始化日志对象
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志格式：级别 时间 文件名[行号] 日志信息
    format="[%(levelname)s] %(asctime)s %(filename)s[line:%(lineno)d] %(message)s",
    # 打印日志的时间
    datefmt="%a, %Y-%m-%d %H:%M:%S",
    # 输出位置
    # 打开日志文件的方式
    filemode="w"
)