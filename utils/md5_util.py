# -*- coding:utf-8 -*-
"""
1. md5是不可逆的，不能解密
2. 所有语言生成的md5串都是一样的
3. 不论字符串多长，生成的md5是等长的
4. 彩虹表：存的所有常用的加密后的密码对应的md5
5. 解密查询，只能解密常用字符：https://www.cmd5.com/
"""

import hashlib
# import md5 # Python2里的引用


def md5Sha3():
    s = '123456'
    m = hashlib.sha3_224(s.encode())  # 长度是224
    print(m.hexdigest())

    m = hashlib.sha3_256(s.encode())  # 长度是256
    print(m.hexdigest())

    m = hashlib.sha3_512(s.encode())  # 长度是512
    print(m.hexdigest())


def md5Key():
    # 生成 MD5
    my_hash = hashlib.md5()
    my_hash.update("123456".encode("utf-8"))  # str.encode()变成bytes类型才能加密
    print(my_hash.hexdigest())


def md5Key2():
    # 双重 MD5 加密
    md5_obj = hashlib.md5("123456".encode("utf-8"))
    str1 = md5_obj.hexdigest()
    md5_obj2 = hashlib.md5(str1.encode("utf-8"))
    print(md5_obj2.hexdigest())


def md5KeySalt():
    # MD5 加盐值(SALT)
    # 加盐是在用户密码加密后，可以再加一个指定的字符串，再次加密，这样，用户密码被破解的概率极低了
    # 如密码是123456：
    random_str = 'dsfka676f9a78#$%^'  # 盐的值
    # 加盐后，密码变为： 123456dsfka676f9a78#$%^
    s = "123456"
    s = s + random_str
    news = str(s).encode()  # 先变成bytes类型才能加密
    m = hashlib.md5(news)  # 创建md5对象
    print(m.hexdigest())  # 获取加密后的字符串


if __name__ == '__main__':
    md5Sha3()
    md5Key()
    md5Key2()
    md5KeySalt()


# 利用md5进行用户登陆网站进行注册之后密码加密的基本事例
#
# import hashlib
# def md5(arg):#这是加密函数，将传进来的函数加密
#     md5_pwd = hashlib.md5(bytes('abc',encoding='utf-8'))  # 或者 md5_pwd = hashlib.md5('abc'.encode('utf-8'))
#     md5_pwd.update(bytes(arg,encoding='utf-8'))
#     return md5_pwd.hexdigest()#返回加密的数据
# def log(user,pwd):#登陆时候时候的函数，由于md5不能反解，因此登陆的时候用正解
#     with open('passwd','r',encoding='utf-8') as f:
#         for line in f:
#             u,p=line.strip().split('|')
#             if u ==user and p == md5(pwd):#登陆的时候验证用户名以及加密的密码跟之前保存的是否一样
#                 return True
# def register(user,pwd):#注册的时候把用户名和加密的密码写进文件，保存起来
#     with open('passwd','a',encoding='utf-8') as f:
#         temp = user+'|'+md5(pwd)
#         f.write(temp)
#
# i=input('1表示登陆，2表示注册：')
# if i=='2':
#     user = input('用户名：')
#     pwd =input('密码：')
#     register(user,pwd)
# elif i=='1':
#     user = user = input('用户名：')
#     pwd =input('密码：')
#     r=log(user,pwd)#验证用户名和密码
#     if r ==True:
#         print('登陆成功')
#     else:
#         print('登陆失败')
# else:
#     print('账号不存在')
