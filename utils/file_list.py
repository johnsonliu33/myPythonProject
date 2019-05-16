# -*- coding:utf-8 -*-
"""遍历文件夹所有文件，计算文件总数和大小"""
import os

count = 0
all_size = 0


def file_list(dir_name):
    dir_list = os.listdir(dir_name)
    for child_name in dir_list:
        if os.path.isdir(os.path.join(dir_name, child_name)):
            dirs = os.path.join(dir_name, child_name)
            file_list(dirs)
        else:
            file_name = os.path.join(dir_name, child_name)
            global count
            count = count + 1
            size = os.path.getsize(file_name)
            global all_size
            all_size = all_size + size
            print(file_name, "  %.3f Kb" % (size / 1024))


def find_files():
    file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    dir_name = os.path.join(file_path, "MyEclipse_WorkSpace")
    print("文件夹", dir_name)
    file_list(dir_name)
    print("共：%d 个文件" % count)
    print("共：%.3f M" % (all_size / 1024 / 1024))


if __name__ == '__main__':
    find_files()
