from msk_package.msk_driver import driver
from selenium.common.exceptions import NoSuchElementException

print("init login")
try:
    imputs = driver.find_elements_by_class_name("android.widget.EditText")
except NoSuchElementException:
    print("no find imputs")
else:
    imputs[0].send_keys("https009")
    imputs[1].send_keys("11111")
try:
    login = driver.find_element_by_class_name("android.widget.TextView")
except NoSuchElementException:
    print("no find login")
else:
    login.click()
    print("to login")
