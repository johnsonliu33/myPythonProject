a = [1, 2, 3]
b = [1, "abc", 3.5, ["789", "qwe", "e234e"]]
print(a)
print(b)

# def print(self, *args, sep=' ', end='\n', file=None)
print(a[0], a[1], a[2], sep="-", end="***\n")  # 1-2-3***
c = b[1:3]
print(c, type(c))  # ['abc', 3.5]  <class 'list'>
print(b[-1])  # ['789', 'qwe', 'e234e']
print(b[3][2])  # e234e

s = "qwertyuiop"
print(s[2:5], s[-1])  # ert p

t = "123456789"
print(t[1:5:2])  # 24
print(t[::2])  # 13579

