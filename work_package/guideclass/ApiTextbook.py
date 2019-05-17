import requests
import json
from urllib import parse


def subject_type(var):
    return {
        "2": "数学",
        "3": "英语",
        "4": "物理",
        "5": "化学",
    }.get(var, "学科不存在！")


def get_textbook():
    uri = "http://gclass.jd100.com/api/getStudentTextbooks"
    username = "https004"
    subject = "2"
    textmod = {"username": username, "subject": subject}
    textmod = parse.urlencode(textmod)
    url = uri + "?" + textmod
    print(url)
    response = requests.get(url)
    data = response.content.decode("utf-8")
    # 把json形式的字符串转换成python形式的Unicode字符串
    json_str = json.loads(data)
    '''
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
    '''
    print(json_str)

    if json_str["success"]:
        grade_type = "高中" if json_str["gradeType"] == "gz" else "初中"
        grade_subject = subject_type(subject)
        print(grade_type)
        print(grade_subject)
        for text_books in json_str["textbooks"]:
            text_book_name = text_books
            text_book_value = json_str["textbooks"][text_books]
            print(text_book_name)
            # print(text_book_value)
            for key_one in text_book_value:
                print(key_one["term"])
                print(key_one["standard"])
                print(key_one["grades"])


if __name__ == "__main__":
    get_textbook()
