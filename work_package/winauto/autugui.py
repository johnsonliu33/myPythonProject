import pyautogui
from pywinauto import Application
import time

# 获取当前屏幕分辨率
screenWidth, screenHeight = pyautogui.size()
print("宽：", screenWidth, "  高：", screenHeight)
# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()
print("X：", screenWidth, "  Y：", screenHeight)

# 启动程序
Application(backend="uia").start("C:\Program Files (x86)\Easytech\EasyClient\EasyClient.exe")
time.sleep(3)
img = pyautogui.screenshot(region=(0, 0, 1600, 900))
img.save('启动程序.png')
# pic_option = pyautogui.locateOnScreen('启动程序.png')
# rec = pyautogui.center(pic_option)

# 鼠标移动坐标为(X, Y)位置 绝对移动
pyautogui.moveTo(675, 431, duration=2, tween=pyautogui.easeInOutQuad)
time.sleep(2)
pyautogui.doubleClick()
pyautogui.press('Del')  # 相当于 pyautogui.keyDown('Del') + pyautogui.keyUp('Del')

# 在每次输入之间暂停0.25秒
pyautogui.typewrite("https002", interval=0.25)
img = pyautogui.screenshot(region=(0, 0, 1600, 900))
img.save('账号.png')

pyautogui.moveTo(675, 476)
time.sleep(2)
pyautogui.doubleClick()
pyautogui.press('Del')
pyautogui.typewrite("11111", interval=0.25)
img = pyautogui.screenshot(region=(0, 0, 1600, 900))
img.save('密码.png')
# 用缓动/渐变函数让鼠标2秒后移动到(X,Y)位置
pyautogui.moveTo(800, 550, duration=2, tween=pyautogui.easeInOutQuad)
# 鼠标左击
pyautogui.click()
img = pyautogui.screenshot(region=(0, 0, 1600, 900))
img.save('登录.png')

# 键盘点击esc
# pyautogui.press("esc")
