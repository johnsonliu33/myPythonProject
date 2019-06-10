# -*- coding:utf-8 -*-
"""遍历文件夹所有文件，计算文件总数和大小;解压所有zip文件"""
import os
import zipfile

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
            count += 1
            size = os.path.getsize(file_name)
            global all_size
            all_size = all_size + size
            print(file_name, "\t%.3f Kb" % (size / 1024))
            if file_name.endswith(".zip"):
                file_zip = zipfile.ZipFile(file_name, "r")
                for f in file_zip.namelist():
                    file_zip.extract(f, dir_name)
                file_zip.close()
                os.remove(file_name)


def find_files():
    file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    dir_name = os.path.join(file_path, "MyEclipse_WorkSpace")
    print("文件夹", dir_name)
    file_list(dir_name)
    print("共：%d 个文件" % count)
    print("共：%.3f M" % (all_size / 1024 / 1024))


if __name__ == '__main__':
    find_files()

    # ########start 获取文件路径、文件名、后缀名############
    # def jwkj_get_filePath_fileName_fileExt(filename):
    #     (filepath, tempfilename) = os.path.split(filename);
    #     (shotname, extension) = os.path.splitext(tempfilename);
    #   return filepath, shotname, extension
