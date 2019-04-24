# +	    加 - 两个对象相加
# -	    减 - 得到负数或是一个数减去另一个数
# *	    乘 - 两个数相乘或是返回一个被重复若干次的字符串
# /	    除 - x除以y
# % 	取余 - 返回除法的余数
# **   	幂 - 返回x的y次幂
# //	取整除 - 返回商的整数部分（向下取整）

# >>>a=1
# >>>b=3
# >>>c=a+b     c=4
# >>>type(c)   <class"int">

# >>>a=1
# >>>b=3
# >>>c=a / b     c=0.66666666666666
# >>>type(c)   <class"float">

# >>>a=4
# >>>b=2
# >>>c=a / b     c=2.0
# >>>type(c)   <class"float">

# >>>a=3
# >>>b=2
# >>>c=a // b     c=1
# >>>type(c)   <class"int">


# 保留两位小数
a = 7.346
b = 5.000

# 方法一
round(a, 2)  # a--小数，2--想保留的小数位数
# 输入结果：7.35
round(b, 2)  # 这里发现不能完全保留两位小数
# 输出结果： 5.0

# 方法二 -----格式化后从数值型变为了字符串
'%.2f' % a
# 输出结果： '7.35'
c = 5
float('%.2f' % c)  # 不可以输出两位数
# 输出结果： 5.0

# 方法三
from decimal import Decimal
Decimal('7.346').quantize(Decimal('0.00'))
Decimal('5.0000').quantize(Decimal('0.00'))




