# 获取元素 8个
driver.find_elements_by_id()
driver.find_element_by_name()
driver.find_element_by_class_name()
driver.find_elements_by_xpath()
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
driver.find_element_by_tag_name()
driver.find_element_by_css_selector()

# 初始化浏览器驱动
driver = webdriver.Firefox(executable_path="../config/geckodriver.exe")
driver = webdriver.Chrome(executable_path="../config/chromedriver.exe")
driver = webdriver.Ie(executable_path="../config/IEDriverServer.exe")

# 浏览器自定义安装路径
option = webdriver.ChromeOptions
option.add_argument("--user-data-dir=C:\Program Files (x86)\Google\Chrome\Application")
driver = webdriver.Chrome(chrome_options=option)