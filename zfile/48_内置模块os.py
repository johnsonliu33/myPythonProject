import os

print(os.getcwd())  # 当前目录
print(os.listdir())  # 当前目录下的文件
os.mkdir("demo")  # 创建文件夹
print(os.path.isdir("demo"))  # 判断demo是不是文件夹  True
print(os.path.isfile("demo"))  # 判断demo是不是文件   False
print(os.path.exists("test.txt"))  # 判断test.txt是否存在    True
print(os.path.exists("demo"))  # 判断demo是否存在    True
print(os.path.join("zfile", "test.txt"))  # 拼接路径   zfile\test.txt
