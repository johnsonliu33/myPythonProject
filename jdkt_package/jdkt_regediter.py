from jdkt_package.jdkt_driver import driver
from selenium.common.exceptions import NoSuchElementException

def regediter():
    print("立即注册")
    try:
        regedit=driver.find_element_by_id("com.jiandan.mobilelesson:id/regist_btn")
    except NoSuchElementException as noSuch:
        print("no find regedit")
    else:
        regedit.click()
