# -*- cocoding:utf-8 -*-


# 一、冒泡排序：
# 每轮依次比较相邻两个数的大小，后面比前面小则交换
def bubble_sort(temp_list):
    for i in range(len(temp_list) - 1):
        for j in range(len(temp_list) - 1):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]
    print(temp_list)


# 二、选择排序思路：
# 拿第一个数与后面数相比较，如果比后面的数大则交换
# 拿第二个数与后面的数比较，如果比后面的数大则交换
# 直到比较到倒数第二个数，最后一个数不用比较
def choice_sort(temp_list):
    for i in range(len(temp_list) - 1):
        for j in range(i + 1, len(temp_list)):
            if temp_list[i] > temp_list[j]:
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
    print(temp_list)


# 三、快速排序思路：
# 选择第一个数为基点，右边 j 开始查找比基点小的数停止，再从左边 i 查找比基点数大的数停住
# 调换 i、j 对应的数后执行步骤 2，直到 i 和 j 相遇，此时 i == j
# 调换 i 对应的数和基点数，将源数列一分为 2 后分别重复步骤 2、3、4，直到结束
def quick_sort(temp_list):
    temp_list.sort()
    print(temp_list)


if __name__ == '__main__':
    temp_list1 = [6, 3, 7, 1, 9, 5, 4, 2, 8]
    bubble_sort(temp_list1)
    temp_list2 = [6, 3, 7, 1, 9, 5, 4, 2, 8]
    choice_sort(temp_list2)
    temp_list3 = [6, 3, 7, 1, 9, 5, 4, 2, 8]
    quick_sort(temp_list3)

# 总结：
# 1、选择排序不稳定，时间复杂度为 O(n2)
# 2、冒泡排序稳定，时间复杂度为 O(n2)
# 3、快速排序不稳定，时间复杂度为 O(nlogn)
# 4、对于 100000 个随机数排序，选择排序约 20s，冒泡排序约 60s，快速排序约 0.02s
