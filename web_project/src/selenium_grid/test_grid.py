# -*- coding:utf-8 -*-
"""
启动hub：
C:\>java -jar selenium-server-standalone-3.141.59.jar -p 4444 -role hub
启动node：
C:\>java -jar selenium-server-standalone-3.141.59.jar  -role node -port 5555 -hub http://localhost:4444/grid/register
打开平台地址：
http://localhost:4444/grid/console
-----------------------------------------------------------------------------------------------------------------------
远程社设备执行命令
C:\>java -jar selenium-server-standalone-3.141.59.jar -role webdriver -hub http:
//localhost:4444/grid/register-Dwebdriver.firefox.driver="D:\myPythonProject\web
_project\driver\geckodriver.exe" -port 6655 - maxSession 5 -browser browserName=
"firefox",maxInstances=5
"""
from selenium import webdriver
from time import sleep

driver = webdriver.Remote(
    # 设置Node节点的URL地址，通过该地址连接到node计算机
    command_executor="http://localhost:6655/wd/hub",
    desired_capabilities={
        # 指定远程计算机执行使用的浏览器为Firefox
        "browserName": "fireFox",
        "video": "True",
        "platform": "WINDOWS"
    })
print("http://www.baidu.com" + driver.session_id)

"""百度搜索python"""
try:
    driver.implicitly_wait(8)
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("python")
    sleep(3)
    driver.find_element_by_id("su").click()
    sleep(3)
    assert "python_百度搜索" in driver.title
    assert "python" in driver.page_source
except:
    pass
finally:
    driver.quit()
