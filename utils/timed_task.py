# -*- coding:utf-8 -*-

import time
import datetime

interval = 1 * 60  #乘以60秒
end_time = datetime.datetime(2019, 7, 25, 13, 20, 0)
while datetime.datetime.now() < end_time:
    print("定时任务..." + datetime.datetime.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(interval)
