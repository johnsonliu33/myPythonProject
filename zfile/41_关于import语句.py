# from sys import path
# print(path)
# 同等于
import sys

print(sys.path)
print(sys.__loader__)

# 引用顺序
# 1.先引入内置库
# 2.然后引入第三方库
# 3.最后引入自己项目的库
