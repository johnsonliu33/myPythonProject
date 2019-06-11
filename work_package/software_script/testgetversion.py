# -*- coding: utf-8 -*-

from ctypes import cdll, c_int, c_char_p, byref
import json


def getCurVersionInfo():
    dll = cdll.LoadLibrary('./PythonGetETClientVersion.dll')
    strversionlen = 0
    outstrlen = c_int(strversionlen)

    try:
        pstr = dll.GetETClientVersionInfo(0, byref(outstrlen))
        strcontent = c_char_p(pstr)

        if outstrlen.value < 50:
            return False, strcontent.value[:outstrlen.value]

        # print strcontent.value[:outstrlen.value]
        rst = json.loads(strcontent.value[:outstrlen.value])
        return True, rst
    except Exception as error:
        print(error.message)
        return False, u'从服务端获取版本信息失败'


if __name__ == "__main__":
    ret, data = getCurVersionInfo()
    print(data)
