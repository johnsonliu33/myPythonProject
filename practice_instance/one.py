# -*- cocoding:utf-8 -*-
"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j)and(i!=k)and(j!=k):
                count+=1
                print(i,j,k)
print("一共 %d 个"  % count)

x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    # false or false or true and true
    #false or false or true
    print(False or False or True) # true
    print(3)
else:
    print(4)