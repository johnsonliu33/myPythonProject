import requests
import re
from time import sleep
url = "https://huke88.com/course/30973.html"
header_dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Cookie": "neplayer_deviceId=15554285728097283375322; setting_line=qn; play_speed=1.25; uv=fa610a2220dc2e597c50a43511328031ae46f76d156667df2f20515cf2a3dacba%3A2%3A%7Bi%3A0%3Bs%3A2%3A%22uv%22%3Bi%3A1%3Bs%3A32%3A%22ee61d9151732273e32350df1f53b42d3%22%3B%7D; REFERRER_SITE=8f38781c313606dc47795e344591e0912219e3b603ae228cfd1d254992bf0c8ea%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22REFERRER_SITE%22%3Bi%3A1%3Bs%3A5%3A%22baidu%22%3B%7D; REFERRER_SITE_KEYWORD=1cae7fe6aa75cd6004aea962fcf5c133feff8ab88d3c9463c60e63ce22c62d62a%3A2%3A%7Bi%3A0%3Bs%3A21%3A%22REFERRER_SITE_KEYWORD%22%3Bi%3A1%3Bs%3A6%3A%22108486%22%3B%7D; REFERRER_STATISTICS_RECHARGE=2201e7e7450e08bcec45ee23319619951086f5e799ec46a390fbfeb63ae52580a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22REFERRER_STATISTICS_RECHARGE%22%3Bi%3A1%3Bi%3A2009%3B%7D; _csrf-frontend=5969238a319f1e295644fed7792dd5e742bba0d45295df31f3898208d008c350a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22rztzvNKu_FQoyQVUlr5wGqLLx08koxYJ%22%3B%7D; Hm_lvt_a0e66ced62f1926ee48b5f059ad9f039=1555428307; IPSTRATIFIED=966e40c1416b75359e7b3f341114a552dfae4dfca5e31e2507764146d446f05ca%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22IPSTRATIFIED%22%3Bi%3A1%3Bi%3A1%3B%7D; FIRSTVISITED=1555428307.118; advanced-frontend=njsicaqj8fvfdf3ejiq379usc4; REFERRER_COME_HOST=298dadf6c35598f14de2184c5427a9add3039a42c2948a566e50f3b75903b7c6a%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22REFERRER_COME_HOST%22%3Bi%3A1%3Bi%3A9%3B%7D; _identity-usernew=4c2198a9ea20e68414c6657f7828a38d3732233070316e4d2f02482cddebe3c7a%3A2%3A%7Bi%3A0%3Bs%3A17%3A%22_identity-usernew%22%3Bi%3A1%3Bs%3A20%3A%22%5B9045031%2C%22%22%2C2592000%5D%22%3B%7D; ISREQUEST=1; WEBPARAMS=is_pay=0; is_show_video_rank_tip=de966eb36605c1941c677243e971bef31f775b8712d271c8b67a302031b068f2a%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22is_show_video_rank_tip%22%3Bi%3A1%3Bi%3A1%3B%7D; Hm_lpvt_a0e66ced62f1926ee48b5f059ad9f039=1555429826"
}
resp = requests.get(url)
# print(resp.text)
cont = resp.text
key = '<p class="video-name" title="(.+?)">.+?</p>'
tempList = re.findall(key, cont)
i = 0
for temp in tempList:
    print(temp.split("章：")[1])
    t = temp.split("章：")[1]
    filename = "../zfile/%d_%s.py" % (i, t)
    with open(filename, "a")as file:
        file.write("")
    i += 1
