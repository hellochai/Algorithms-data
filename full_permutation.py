#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 15:28
# @Author  : fchai
# @Desc    :
# @File    : full_permutation.py
# @Software: PyCharm

""" 全排列
# 如 n=3,则三个数1，2，3的全排列有
    123,132,213,231,312,321

    每确定一个位的数时，其他位做交换
"""
import math


def full_permutation(number, n):

    if len(number) == 3:return number
    for i in range(1, n):
        print("i: ", i)
        number += str(i) + full_permutation(str(i), n - 1)

    return number


# x的阶乘
def get(x, n):
    num = 0
    for i in range(1, n):
        num += math.pow(x, n)
    return int(num)


if __name__ == '__main__':
    # full_permutation("",3)
    print("x的阶乘", get(2, 3))