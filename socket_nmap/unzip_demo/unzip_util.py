# -*- coding:utf-8 -*-

"""暴力破解zip文件"""

from optparse import OptionParser
import zipfile
from threading import Thread


def extractFile(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        print("[+] Found Password : " + password)
    except:
        pass


def main():
    usage = "[*] Usage : %prog -f <zipfile> -d <dictionnary file>"
    parse = OptionParser(usage)
    parse.add_option("-f", dest="zname", type="string", help="specify zip file")
    parse.add_option("-d", dest="dname", type="string", help="specify password file")
    (options, args) = parse.parse_args()
    if (options.zname is None) | (options.dname is None):
        print(parse.usage)
        exit(0)
    zip_file = options.zname
    password_file = options.dname
    zFile = zipfile.ZipFile(zip_file)
    passFile = open(password_file)
    for line in passFile.readlines():
        password = line.split("\n")
        test = Thread(target=extractFile, args=(zip_file, password))
        test.start()


if __name__ == "__main__":
    main()
