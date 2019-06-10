test_list = ["1", "2", "3", "4", "5"]
seq = {"a", "b", "c", "4", "5"}
# len(list) 	返回列表长度
print(len(test_list))  # 输出：5
# max（list） 	返回列表中最大的元素
print(max(test_list))  # 输出：5
# min(list) 	返回列表中的最小值
print(min(test_list))  # 输出：1
# list(seq) 	将元组转为列表
print(list(seq))  # 输出：['c', 'a', '4', '5', 'b']

name_list = ["123", "Tom", "Marry", "Alex", "thea"]

#  	list.append(obj) 	在列表末尾添加新的对象
name_list.append("thea")
print("append：{}".format(name_list))  # 输出：['123', 'Tom', 'Marry', 'Alex', 'thea', 'thea']

#  	list.count(obj) 	统计某个元素在列表中出现的次数
cou = name_list.count("thea")
print("count：{}".format(cou))  # 输出：2

#  	list.extend(seq) 	在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
name_list.extend(name_list)  # 等同于 list1+list2
print("extend：{}".format(
    name_list))  # 输出：['123', 'Tom', 'Marry', 'Alex', 'thea', 'thea', '123', 'Tom', 'Marry', 'Alex', 'thea', 'thea']

#  	list.index(obj) 	从列表中找出某个值第一个匹配项的索引位置
num = name_list.index("thea")
print("index：{}".format(num))  # 输出：3

# 	list.insert(index, obj) 	将对象插入列表
name_list.insert(1, "Lily")
print("insert：{}".format(
    name_list))  # 输出：['123', 'Lily', 'Tom', 'Marry', 'Alex', 'thea', 'thea', '123', 'Tom', 'Marry', 'Alex', 'thea', 'thea']

#  	list.pop([index=-1]]) 	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
name_list.pop()
print("pop：{}".format(
    name_list))  # 输出：['123', 'Lily', 'Tom', 'Marry', 'Alex', 'thea', 'thea', '123', 'Tom', 'Marry', 'Alex', 'thea']

# 	list.remove(obj) 	移除列表中某个值的第一个匹配项
obj = "Tom"
name_list.remove(obj)
print("remove：{}".format(
    name_list))  # 输出：['123', 'Lily', 'Marry', 'Alex', 'thea', 'thea', '123', 'Tom', 'Marry', 'Alex', 'thea']

#  	list.reverse() 	反向列表中元素
name_list.reverse()
print("reverse：{}".format(
    name_list))  # 输出：['thea', 'Alex', 'Marry', 'Tom', '123', 'thea', 'thea', 'Alex', 'Marry', 'Lily', '123']

# 	list.sort(cmp=None, key=None, reverse=False) 	对原列表进行排序
name_list.sort()
print("sort 正序 ：{}".format(
    name_list))  # 输出：['123', '123', 'Alex', 'Alex', 'Lily', 'Marry', 'Marry', 'Tom', 'thea', 'thea', 'thea']
name_list.sort(reverse=True)
print("sort 倒叙 ：{}".format(
    name_list))  # 输出：['thea', 'thea', 'thea', 'Tom', 'Marry', 'Marry', 'Lily', 'Alex', 'Alex', '123', '123']

# 	name_list.copy() 	复制列表
name_list2 = name_list.copy()
print("copy ：{}".format(
    name_list2))  # 输出：['thea', 'thea', 'thea', 'Tom', 'Marry', 'Marry', 'Lily', 'Alex', 'Alex', '123', '123']
name_list2[0] = "999"
print(name_list2)  # 输出：['999', 'thea', 'thea', 'Tom', 'Marry', 'Marry', 'Lily', 'Alex', 'Alex', '123', '123']

#  	list.clear() 	清空列表
name_list.clear()
print("clear ：{}".format(name_list))  # 输出：[]
