# -*- coding:utf-8 -*-

import os
import datetime
from config.varConfig import screenPicturesDir


# 获取当前的日期
def getCurrentDate():
    currentDate = datetime.date.today()
    return currentDate

# 获取当前的时间
def getCurrentTime():
    timeStr= datetime.datetime.now()
    nowTime =timeStr.strftime("%H - %M - %S - %f")
    return nowTime

# 创建截图存放的目录
def ceateCurrentDateDie():
    dirName= os.path.join(screenPicturesDir,str(getCurrentDate()))
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    return dirName

if __name__ == '__main__':
    print(getCurrentDate())
    print(getCurrentTime())
    print(ceateCurrentDateDie())