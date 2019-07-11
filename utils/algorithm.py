# -*- cocoding:utf-8 -*-


# 一、冒泡排序：
# 每轮依次比较相邻两个数的大小，后面比前面小则交换
def bubble_sort(temp_list):
    n=len(temp_list)
    for i in range(n):
        for j in range(n-i-1):
            if temp_list[j]>temp_list[j+1]:
                temp_list[j],temp_list[j+1]=temp_list[j+1],temp_list[j]
    print(temp_list)


# 二、选择排序思路：
# 拿第一个数与后面数相比较，如果比后面的数大则交换
# 拿第二个数与后面的数比较，如果比后面的数大则交换
# 直到比较到倒数第二个数，最后一个数不用比较
# 两个数比较可以用中间变量替换或者位运算
# 利用位运算时需注意，如果两个数相等则不能使用位运算




# 三、快速排序思路：
# 选择第一个数为基点，右边 j 开始查找比基点小的数停止，再从左边 i 查找比基点数大的数停住
# 调换 i、j 对应的数后执行步骤 2，知道 i 和 j 相遇，此时 i == j
# 调换 i 对应的数和基点数，将源数列一分为 2 后分别重复步骤 2、3、4，知道结束
# 注意使用位运算调换时必须判断交换两个数不能相等，否则第二个数为 0


if __name__ == '__main__':
    temp_list=[3,7,1,5,4,2,8,0]
    bubble_sort(temp_list)





# 总结：
# 1、选择排序不稳定，时间复杂度为 O(n2)
# 2、冒泡排序稳定，时间复杂度为 O(n2)
# 3、快速排序不稳定，时间复杂度为 O(nlogn)
# 4、对于 100000 个随机数排序，选择排序约 20s，冒泡排序约 60s，快速排序约 0.02s