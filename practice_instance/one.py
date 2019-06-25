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


# 数字求和
# 平方根
# 二次方程
# 计算三角形的面积
# 计算圆的面积
# 随机数生成
# 摄氏温度转华氏温度
# 交换变量
# if 语句
# 判断字符串是否为数字
# 判断奇数偶数
# 判断闰年
# 获取最大值函数
# 质数判断
# 输出指定范围内的素数
# 阶乘实例
# 九九乘法表
# 斐波那契数列
# 阿姆斯特朗数
# 十进制转二进制、八进制、十六进制
# ASCII码与字符相互转换
# 最大公约数算法
# 最小公倍数算法
# 简单计算器实现
# 生成日历
# 使用递归斐波那契数列
# 文件 IO
# 字符串判断
# 字符串大小写转换
# 计算每个月天数
# 获取昨天日期
# list 常用操作
# 约瑟夫生者死者小游戏
# 实现秒表功能
# 计算 n 个自然数的立方和
# 计算数组元素之和
# 数组翻转指定个数的元素
# 将列表中的头尾两个元素对调
# 将列表中的指定位置的两个元素对调
# 翻转列表
# 判断元素是否在列表中存在
# 清空列表
# 复制列表
# 计算元素在列表中出现的次数
# 计算列表元素之和
# 计算列表元素之积
# 查找列表中最小元素
# 查找列表中最大元素
# 移除字符串中的指定位置字符
# 判断字符串是否存在子字符串
# 判断字符串长度
# 使用正则表达式提取字符串中的 URL
# 将字符串作为代码执行
# 字符串翻转
# 对字符串切片及翻转
# 按键(key)或值(value)对字典进行排序
# 计算字典值之和
# 移除字典点键值(key/value)对
# 合并字典
# 将字符串的时间转换为时间戳
# 获取几天前的时间
# 将时间戳转换为指定格式日期
# 打印自己设计的字体
# 二分查找
# 线性查找
# 插入排序
# 快速排序
# 选择排序
# 冒泡排序
# 归并排序
# 堆排序
# 计数排序
# 希尔排序
# 拓扑排序