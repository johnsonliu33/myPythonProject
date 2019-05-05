import requests


def gethtml():
    headers = {"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
               "Accept-Encoding: gzip, deflate, br",
               "Accept-Language: zh-CN,zh;q=0.9",
               "Connection: keep-alive",
               "Host: vip.jd100.com",
               "Upgrade-Insecure-Requests: 1"}
    url = "https://vip.jd100.com/g1/freelesson/"
    response = requests.get(url)
    # print(response.encoding)
    html = response.content
    html_doc = str(html, "utf-8")

    return html_doc


def getcontent(htmltxt):
    # print(htmltxt)
    # 内容分割的标签
    str1 = 'freeLessonRow clearfix'
    content = htmltxt.partition(str1)[2]
    # print(content)
    str2 = 'embed'
    content = content.partition(str2)[0]
    # print(content)
    return content  # 得到网页的内容


def gettitle(content, beg=0):
    # 思路是利用str.index()和序列的切片
    try:
        title_list = []
        while True:
            num1 = content.index('"free_lessonTil">', beg)
            num2 = content.index('</dd>', num1)
            temp = content[num1: num2]
            titl = temp.split('>')
            title_list.append(titl[1])
            beg = num2
    except ValueError:
        return title_list


if __name__ == "__main__":
    resp = gethtml()
    freeLesson = getcontent(resp)
    lessonTil = gettitle(freeLesson)
    for less in lessonTil:
        print(less)
