from appium import webdriver

print("init myDriver")
desired_caps = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62025",
    "appPackage": "com.jiandan.mobilelesson",
    "appActivity": "com.jiandan.mobilelesson.InstallOpenActivity",
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true',
    "noReset": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
driver.implicitly_wait(3)  # 隐式等待3秒
print("start appPackage")
