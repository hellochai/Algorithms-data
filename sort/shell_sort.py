#! /usr/bin/python
# 希尔排序

def insert_sort(arr):
    """
    将一个数插入到一个有序序列：将关键字与有序序列最后一个数比较，若大于最有一个数，则不用与前边的数比较，反之则将前一个数后移，
    将关键字赋值到前一个数的位置，依次循环比较。
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        key = arr[i]
        if key > arr[i - 1]:
            continue
        j = i - 1
        while j >= 0:
            if arr[j] < key:
                j -= 1
                break
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1
    return arr


# 希尔排序
# 考虑插入排序，若已知序列与要求序列完全相反，则需要将数据挨个依次后移，排序难度大
# 希尔排序是将序列逐步差分为多个小序列，在每个序列内在使用插入排序

def shell_sort(arr):
    if len(arr) == 1:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        if key > arr[i - 1]:
            continue
        j = i - 1
        while j >= 0:
            if arr[j] < key:
                j -= 1
                break
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1

    index = len(arr) // 2
    arr = shell_sort(arr[:index]) + shell_sort(arr[index:])
    return arr


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 6, 4, 10, 11, 2]
    print("插入排序:", insert_sort(arr))
    print("希尔排序:", shell_sort(arr))
