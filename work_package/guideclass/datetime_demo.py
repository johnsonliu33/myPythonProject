# -*- coding:utf-8 -*-
import datetime

# 当前日期时间
print(datetime.datetime.now())
# 格式化时间
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# 多加一天
print((datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
# 减一天
print((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d %H:%M:%S"))
# 可以把days改为 hours / minutes，就可以提前XX小时/分钟。
meeting_date = datetime.datetime(2019, 5, 13, 6, 30, 0) + datetime.timedelta(hours=-8)
print(meeting_date)
#格式化指定时间为UTC时间
meeting_date = datetime.datetime(2019, 5, 13, 6, 30, 0)
print(meeting_date)

now_time = datetime.datetime.now()  # 获取当地时间，2018-10-07 20:26:52.608251
now_ = datetime.datetime.strftime(now_time, '%Y-%m-%d')  # 转换为字符串并格式化，2018-10-07
now_1 = datetime.datetime.strptime(now_, '%Y-%m-%d')  # 将str转化为datetime并格式化，2018-10-07 00:00:00
timestamp = datetime.datetime.timestamp(now_time)  # 转换为时间戳，1538915212.608251
now = datetime.datetime.fromtimestamp(timestamp)  # 时间戳转换为本地时间，2018-10-07 20:26:52.608251
utc = datetime.datetime.utcfromtimestamp(timestamp)  # 时间戳转换为格林时间，2018-10-07 12:31:19.632581
utc_time = datetime.datetime.utcnow()  # 获取格林时间，2018-10-07 12:26:52.608251
now_time1 = utc_time + datetime.timedelta(hours=+8)  # 格林时间转换为本地时间，2018-10-07 20:26:52.608251
time = now_time + datetime.timedelta(days=1, hours=1)  # datetime加减，2018-10-08 21:41:25.363386
