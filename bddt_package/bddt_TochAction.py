import time

from bddt_package.bddt_driver import driver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

x = driver.get_window_size()["width"]
y = driver.get_window_size()["height"]


def pinch():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.2, y=y * 0.2).wait(1000).move_to(x=x * 0.4, y=y * 0.4).wait(1000)
    action2.press(x=x * 0.8, y=y * 0.8).wait(1000).move_to(x=x * 0.6, y=y * 0.6).wait(1000)
    zoom_action.add(action1, action2)
    zoom_action.perform()


def zoom():
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x * 0.4, y=y * 0.4).wait(1000).move_to(x=x * 0.2, y=y * 0.2).wait(1000)
    action2.press(x=x * 0.4, y=y * 0.6).wait(1000).move_to(x=x * 0.8, y=y * 0.8).wait(1000)
    zoom_action.add(action1, action2)
    zoom_action.perform()


def move():
    TouchAction(driver).press(x=243, y=381).wait(2000) \
        .move_to(x=455, y=390).wait(1000) \
        .move_to(x=643, y=584).wait(1000) \
        .move_to(x=647, y=784).wait(1000) \
        .release().perform()


pinch()
time.sleep(10)
zoom()
time.sleep(10)
move()
