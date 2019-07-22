# -*- coding:utf-8 -*-

import os
import sys


def dump(dn_name):
    DATA_BASE = dn_name  # 库名
    DBUSER = "guideclass"  # 用户
    DBPASS = "zaq1xsw2"  # 密码
    IP = "172.16.0.166"  # 主机
    DATA_DIR = "./back_data"  # 目录
    PATH_DUMP = "/usr/local/mongodb/bin/mongodump"  # 命令路径
    BACKITEMS = ['%s -h %s:27017 -u %s -p %s -d %s -o %s' % (PATH_DUMP, IP, DBUSER, DBPASS, DATA_BASE, DATA_DIR),
                 'date +"%Y-%m-%d %T"']
    mk_dir = "mkdir back_data"
    if not os.path.exists("back_data"):
        os.system(mk_dir)
    try:
        for item in BACKITEMS:
            print("============" + item + "============")
            print(os.system(item))
    except RuntimeError as e:
        print("------" + e + "------")


def main():
    usage = " [-]usage: dump_mongo.py <DATA_BASE> \n     eg : python dump_mongo.py guideclass_ceshi "
    if len(sys.argv) < 2:
        print(usage)
    else:
        dump(sys.argv[1])


if __name__ == '__main__':
    main()
