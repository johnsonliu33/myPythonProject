# -*- coding:utf-8 -*-
"""
1. md5是不可逆的，不能解密
2. 所有语言生成的md5串都是一样的
3. 不论字符串多长，生成的md5是等长的
4. 彩虹表：存的所有常用的加密后的密码对应的md5
5. 解密查询，只能解密常用字符：https://www.cmd5.com/
"""
import hashlib
from random import random

import hashlib
#import md5 # Python2里的引用
s='123456'
# s.encode()#变成bytes类型才能加密
m= hashlib.md5(s.encode())
print(m.hexdigest())

m=hashlib.sha3_224(s.encode()) #长度是224
print(m.hexdigest())

m=hashlib.sha3_256(s.encode())  #长度是256
print(m.hexdigest())

m=hashlib.sha3_512(s.encode()) #长度是512
print(m.hexdigest())

def md5Key():
    # 生成 MD5
    my_hash = hashlib.md5()
    my_hash.update("11111".encode("utf-8"))
    print(my_hash.hexdigest())


def md5Key2():
    # 双重 MD5 加密
    md5_obj = hashlib.md5("11111".encode("utf-8"))
    str1 = md5_obj.hexdigest()
    md5_obj2 = hashlib.md5(str1.encode("utf-8"))
    print(md5_obj2.hexdigest())


def md5KeySalt():
    # MD5 加盐值(SALT)
    # 加盐是在用户密码加密后，可以再加一个指定的字符串，再次加密，这样，用户密码被破解的概率极低了

    #如密码是123456：
    random_str='dsfka676f9a78#$%^' # 盐的值
    #加盐后，密码变为： 123456dsfka676f9a78#$%^

    def my_md5(s,salt=random_str):      #加盐，盐的默认值是空
        s=s+salt
        news=str(s).encode()    #先变成bytes类型才能加密
        m=hashlib.md5(news)     #创建md5对象
        return m.hexdigest()    #获取加密后的字符串

if __name__ == '__main__':
    md5Key()
    md5Key2()
