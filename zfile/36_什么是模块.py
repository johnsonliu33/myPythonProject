# -*-coding:utf-8-*-

# 模块
# 模块式一个包含所有定义的函数和变量的文件，后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。


# import 语句
# 想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
# import module1[, module2[,... moduleN]


# from … import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
# from modname import name1[, name2[, ... nameN]]

# __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#
# #!/usr/bin/python3
# # Filename: using_name.py
#
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
# 运行输出如下：
#
# $ python using_name.py
# 程序自身在运行
# $ python
# >>> import using_name
# 我来自另一模块
# >>>
