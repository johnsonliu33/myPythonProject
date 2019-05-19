import os

print(os.getcwd())  # 当前目录
print(os.listdir())  # 当前目录下的文件
# os.mkdir("demo")  # 创建文件夹
print(os.path.isdir("demo"))  # 判断demo是不是文件夹  True
print(os.path.isfile("demo"))  # 判断demo是不是文件   False
print(os.path.exists("test.txt"))  # 判断test.txt是否存在    True
print(os.path.exists("demo"))  # 判断demo是否存在    True
print(os.path.join("zfile", "test.txt"))  # 拼接路径   zfile\test.txt
print(os.path.getsize("test.txt"))  # 获取文件大小

# 关于阻塞调用
# 1.os.popen
# 该命令会先创建一个管道，然后fork一个子进程，关闭管道的一端，执行exec，最后返回一个标准的io文件指针。
# popen本身是不阻塞的，要通过标准io的读取使它阻塞
#
# 2.os.system
# system相当于是先后调用了fork， exec，waitpid来执行外部命令
# system本身就是阻塞的。
# 两者的区别是：
#
# os.system(cmd)的返回值是脚本的退出状态码，只会有0(成功),1,2
# os.popen(cmd)返回脚本执行的输出内容作为返回值
