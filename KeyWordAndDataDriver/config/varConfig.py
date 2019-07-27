# -*- coding:utf-8 -*-
import os

# 获取当前文件所在目录的父目录的绝对路径
parentDirPath= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ieDriverFilePath = os.path.join(parentDirPath, "driver", "IEDriverServer.exe")
chromeDriverFilePath = os.path.join(parentDirPath, "driver", "chromedriver.exe")
firefoxDriverFilePath = os.path.join(parentDirPath, "driver", "geckodriver.exe")

