import requests
from bs4 import BeautifulSoup

headers = {"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
           "Accept-Encoding: gzip, deflate, br",
           "Accept-Language: zh-CN,zh;q=0.9",
           "Connection: keep-alive",
           "Host: vip.jd100.com",
           "Upgrade-Insecure-Requests: 1"}
url = "https://vip.jd100.com/"
session = requests.session()
response = session.get(url)
param = {"fromurl": "https://vip.jd100.com/"}
session = session.get(url="https://vip.jd100.com/user/logon/", params=param)
print(session.cookies)
