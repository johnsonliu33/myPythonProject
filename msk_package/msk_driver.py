from appium import webdriver

print("init myDriver")
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.guideclasspad",
    "appActivity": "com.guideclasspad.MainActivity",
    "unicodeKeyboard": "true",
    "resetKeyboard": "true",
    "noReset": "true"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(8)  # 隐式等待3秒
print("start guideclasspad")
