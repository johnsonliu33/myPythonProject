# -*- coding:utf-8 -*-

import time
import datetime

interval = 1 * 60
end_time = datetime.datetime(2019, 7, 25, 13, 32, 0)
while datetime.datetime.now() <= end_time:
    print("定时任务..." + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(interval)
print("定时任务结束！！！")