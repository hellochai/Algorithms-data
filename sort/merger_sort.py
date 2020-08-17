#!/usr/bin/python
# 归并排序: 将序列分成多个有序序列(一个元素)
# 然后将有序序列进行合并


def merger_sort(left_, right_):
    # 将两个序列合并排序
    r = []
    i = j = 0  # i为left的索引，j为right的索引
    while i < len(left_) and j < len(right_):
        if left_[i] > right_[j]:
            r.append(right_[j])  # 将较小的插入新的列表
            j += 1
        else:
            r.append(left_[i])
            i += 1
    r += left_[i:]
    r += right_[j:]
    return r


def m_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_l = m_sort(arr[:mid])
    right_l = m_sort(arr[mid:])

    return merger_sort(left_l, right_l)


def mergesort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2  # 将列表分成更小的两个列表
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到result中，并对当前列表下标加1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


seq = [5, 3, 0, 6, 1, 4]
print('排序前：', seq)
result = mergesort(seq)
print('排序后：', result)
if __name__ == '__main__':
    arr = [4, 3, 5, 4, 6, 4, 10, 11, 2]
    print(m_sort(arr))
