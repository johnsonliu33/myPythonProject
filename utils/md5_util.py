# -*- coding:utf-8 -*-
import hashlib
from random import random


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
    hashlib.md5


if __name__ == '__main__':
    md5Key()
    md5Key2()
