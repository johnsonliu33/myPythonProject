from jdkt_package.jdkt_driver import driver
from selenium.common.exceptions import NoSuchElementException
import random
print("init regedit")
try:
    regedit = driver.find_element_by_id("com.jiandan.mobilelesson:id/regist_btn")
except NoSuchElementException:
    print("no find regedit")
else:
    regedit.click()
    print("to regedit ")

uname="jdkt"+str(random.randint(10000,99999))
username = driver.find_element_by_id("com.jiandan.mobilelesson:id/user_name").send_keys(uname)
passwd = "11111"
password = driver.find_element_by_id("com.jiandan.mobilelesson:id/password").send_keys(passwd)

driver.find_element_by_id("com.jiandan.mobilelesson:id/gradetv").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/grade").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/year").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/confirm").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/school").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/province").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/city").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/district").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/confirm").click()

iphone="13344"+str(random.randint(100000,999999))
driver.find_element_by_id("com.jiandan.mobilelesson:id/cellphone").send_keys(iphone)
driver.find_element_by_id("com.jiandan.mobilelesson:id/getcheckcode").click()
driver.find_element_by_id("com.jiandan.mobilelesson:id/checkcode").send_keys("123456")
driver.find_element_by_id("com.jiandan.mobilelesson:id/use_regist").click()
driver.close()