# 读写二进制文件必须用wb 或者rb

f = open("test.txt", "wb")
f.write(b"hello world")
f.close()

f = open("test.txt", "rb")
txt = f.read()
print(txt)
f.close()
