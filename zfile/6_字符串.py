a = 'test'
a = "test"
a = "中文"
a = '''三个单引号中可以存在(")和('),不需要转译'''

s = "abcde"
s[0]  # 输出a
s[4]  # 输出e
s[-1]  # 输出e

e = "1"
f = "2"
g = e + f  # g="12"

t = "abc"
y = t * 2  # y="abcabc"

# 判断字符串首字母或结尾字母
str_s = "!fdi$@$sa"
if isinstance(str_s, str):
    print(str_s.startswith("!"))  # True
    print(str_s.endswith("a"))  # True
