# coding=utf-8
from appium import webdriver

print("init myDriver")
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.baidu.BaiduMap",
    "appActivity": "com.baidu.baidumaps.WelcomeScreen",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true",
    "automationName": "uiautomator2",  # 启动device失败时，使用管理员运行appium
    "noReset": "true"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
driver.implicitly_wait(8)  # 隐式等待3秒
print("start appPackage")
