from jdkt_package.jdkt_driver import driver
from selenium.webdriver.support.ui import WebDriverWait

username = driver.find_element_by_id("com.jiandan.mobilelesson:id/account_et")
username.clear()
username.send_keys("https005")

password = driver.find_element_by_id("com.jiandan.mobilelesson:id/password_et")
password.clear()
password.send_keys("1111")

login = driver.find_element_by_id("com.jiandan.mobilelesson:id/login_btn").click()
error_message = r"账号或者密码不正确"
message3 = '//*[@text=\'{}\']'.format(error_message)
try:
    login_element = WebDriverWait(driver, 8, 0.01).until(lambda x: x.find_element_by_xpath(message3))
except:
    driver.get_screenshot_as_file("./image/login_error.png")
else:
    print(login_element.text)
