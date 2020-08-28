#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 10:37
# @Author  : fchai
# @Desc    :
# @File    : basic_sort.py
# @Software: PyCharm

"""
    基数排序:
        1. 低位优先多关键字排序
        
            首先按关键字K^(d-1)进行排序
            然后按关键字K^(d-2)进行排序，依次类推，直到最后
            最主位关键字K0排序完成为止

             按照数据的每一位进行排序

        2. 实现：
            排序三位数：
            1. 使用桶+链表：
                创建两组0-9 10个指针，每组指针分别指向桶的顶和底，
                遍历序列，将个，十，百位的数字与指针序号对应的入桶，将桶的顶与底连接起来，构成链表
                每一位都如此操作，即可实现排序。
"""


def basic_sort(data, k):
    while k >= 0:

        dic = {}
        for i in data:
            num = str(i)
            if num[k] not in dic:
                dic[num[k]] = [num]
            else:
                dic[num[k]].append(num)

        print("result: ", dic)
        k -= 1
        keys_list = sorted(dic)
        print("sort_keys", keys_list)
        new_data = []
        for j in keys_list:
            new_data += dic[j]

        print("res", new_data)

        return basic_sort(new_data, k)


if __name__ == '__main__':
    arr = ["001", 233, 525, 363, 555, 278, 101, 101, "002"]
    basic_sort(arr, 2)
