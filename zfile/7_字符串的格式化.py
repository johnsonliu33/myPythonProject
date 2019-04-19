name = "史瑞克"
age = 28

# 打印：我叫史瑞克，今年28岁啦

new_str1 = "我叫" + name + "," + "今年" + str(age) + "岁啦"
print(new_str1)

new_str2 = "我叫%s，今年%d岁啦" % (name, age)
print(new_str2)

new_str3 = "我叫{}，今年{}岁啦".format(name, age)
print(new_str3)

new_str4 = "我叫{key1}，今年{key2}岁啦".format(key1=name, key2=age)
print(new_str4)

name_s = "史泰龙"
age_s = 55
new_str4 = f"我叫{name_s}，今年{age_s}岁啦"
print(new_str4)
