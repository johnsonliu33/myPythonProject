# def print(self, *args, sep=' ', end='\n', file=None): pass
# sep=' ' 表示插入值之间的字符串，默认为空格;
# end='\n'表示在最后一个值之后追加的字符串，默认为换行;
# file=None 表示输出文件位置，默认为当前sys.stdout
print("hello word", "python", sep="-", end="***")  # hello word-python***
import sys

sys.stdout.write("\n are you ok!")  # are you ok!
