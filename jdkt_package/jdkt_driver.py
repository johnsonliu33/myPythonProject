from appium import webdriver

print("init myDriver")
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.jiandan.mobilelesson",
    "appActivity": "com.jiandan.mobilelesson.InstallOpenActivity",
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true',
    "noReset": True
}
try:
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
except:
    print("init driver error")
else:
    driver.implicitly_wait(8)  # 隐式等待3秒
    print("start appPackage")
