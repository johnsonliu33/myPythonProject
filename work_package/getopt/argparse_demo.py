# -*- coding:utf-8 -*-
"""将源目录中的图片用MD5重命名后移动或复制到目标文件夹"""

import os
# 获取文件类型库
import imghdr
# MD5库
import hashlib
# 文件操作库
import shutil
# 命令行解析库
import argparse


class ArgParseDemo:
    def __init__(self):
        # 初始化argparse
        descrip = "Move or copy the images in the source directory with the name of MD5 into the target directory"
        self.parser = argparse.ArgumentParser(description=descrip)

    ###定义出错文件
    def error_usage(self, res):
        print("[-]error: " + res)
        self.parser.print_usage()
        exit()

    ###计算MD5值
    def md5_util(self, filepath):
        with open(filepath, "rb")as file:
            md5obj = hashlib.md5()
            md5obj.update(file.read())  # 使用提供的字符串更新此哈希对象的状态。
            hash = md5obj.hexdigest()  # 以十六进制数字串的形式返回值
            return hash

    ###找到源目录下所有图片文件
    def find_image(self, source_dir):
        images = []
        # 如果目录不存在，错误退出
        if not os.path.exists(source_dir):
            self.error_usage("Source directory is not defined")
            # 循环目录中的文件
        for files in os.listdir(source_dir):
            # 获取文件的路径
            filepath = os.path.join(source_dir, files)
            # 判断文件是否为目录
            if not os.path.isdir(filepath):
                # 判断文件是否是图片
                if imghdr.what(filepath) is not None:
                    # 将图片存入列表
                    images.append(filepath)
            else:  # 若文件是目录，递归遍历文件，有图片就存入images集合
                self.find_image(filepath)
        return images

    ###处理所有图片
    def image_to_md5(self, target_dir, image_list, operation):
        # 如果目标目录不存在，则报错退出
        if not os.path.exists(target_dir):
            self.error_usage("Target directory is not defined")
        method = {
            "move": shutil.move,
            "copy": shutil.copy
        }
        # 循环处理图片
        for img in image_list:
            print(img)
            # 根据图片的帧数后缀，来确定图片的后缀，如果是jpeg则改成jpg
            postfix = "jpg" if imghdr.what(img) == "jpeg" else imghdr.what(img)
            # 执行复制或移动操作
            method[operation](img, target_dir + "/" + self.md5_util(img) + "." + postfix)

    def main(self):
        # 定义脚本版本
        self.parser.add_argument("-v", "--version", action="version", version="%(prog)s")
        # 添加源参数目录参数,必填
        self.parser.add_argument("sourceDir", help="Select source directory")
        # 添加目标目录参数,选填
        self.parser.add_argument("targetDir", help="Select target directory", nargs="?")
        # 定义一个互相排斥的参数,copy or move 不可同时存在
        group = self.parser.add_mutually_exclusive_group()
        group.add_argument("-m", "--move", help="The way to operate the file is to move", action="store_true")
        group.add_argument("-c", "--copy", help="The way to operate the file is to copy", action="store_true")
        # 将参数变为变量args
        args = self.parser.parse_args()
        # 设置默认参数
        source_dir = args.sourceDir
        target_dir = args.sourceDir or args.tarfetDir
        operation = "copy" if args.copy == True else "move"
        image_list = self.find_image(source_dir)
        self.image_to_md5(target_dir, image_list, operation)


if __name__ == '__main__':
    argp = ArgParseDemo()
    argp.main()
    # usage: argparse_demo.py [-h] [-v] [-m | -c] sourceDir [targetDir]
    #       eg: python argparse_demo.py -c F:\sc_all
    print("Finish")
