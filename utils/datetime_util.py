# -*- coding:utf-8 -*-
import datetime

# 获取当地时间，2018-10-07 20:26:52.608251
now_time = datetime.datetime.now()
# 转换为字符串并格式化，2018-10-07
str_time = datetime.datetime.strftime(now_time, '%Y-%m-%d')
# 将str转化为datetime并格式化，2018-10-07 00:00:00
date_time = datetime.datetime.strptime(str_time, '%Y-%m-%d')
# 转换为时间戳，1538915212.608251
timestamp = datetime.datetime.timestamp(now_time)
# 时间戳转换为本地时间，2018-10-07 20:26:52.608251
now = datetime.datetime.fromtimestamp(timestamp)
# 时间戳转换为格林时间，2018-10-07 12:31:19.632581
utc = datetime.datetime.utcfromtimestamp(timestamp)
# 获取格林时间，2018-10-07 12:26:52.608251
utc_time = datetime.datetime.utcnow()
# 格林时间转换为本地时间，2018-10-07 20:26:52.608251
new_time = utc_time + datetime.timedelta(hours=+8)
# datetime加减，2018-10-08 21:41:25.363386
time = now_time + datetime.timedelta(days=1, hours=1)
# 格式化时间
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# 或者
time.strftime("%Y_%m_%d %H_%M_%S")
# 多加一天
(datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
# 减一天
(datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S")
# 可以把days改为 hours / minutes，就可以提前XX小时/分钟。
utc_time = datetime.datetime(2019, 5, 13, 6, 30, 0) + datetime.timedelta(hours=-8)
