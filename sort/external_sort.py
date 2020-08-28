#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 12:01
# @Author  : fchai
# @Desc    :
# @File    : external_sort.py
# @Software: PyCharm

"""
    外排序
        1. 预处理姐u的那： 根据内存的大小将一个有n个记录的文件分批读入内存，用各种内排序算法排序，
        形成一个个有序片段
        2. 归并阶段： 将这这些有序片段逐步归并成一个有序文件
"""

