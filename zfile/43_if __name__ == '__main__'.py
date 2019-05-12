# main函数只有在自己模块内执行时才会调用
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果在模块被引入时，模块中的某一程序块不执行，
# 可以用__name__属性来使该程序块仅在该模块自身运行时执行。

#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
# 运行输出如下：

# $ python using_name.py
# 程序自身在运行
# $ python
# >>> import using_name
# 我来自另一模块
# >>>
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
#
# 说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格