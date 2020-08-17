# 简单选择排序
# 从未排序的序列中找出最大或者最小的元素加入到有序序列

def choose_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        index = 0
        for j in range(i, len(arr)):
            if arr[j] <= key:
                key = arr[j]
                index = j

        arr[i], arr[index] = arr[index], arr[i]

    return arr


if __name__ == '__main__':
    arr = [4, 3, 5, 4, 6, 4, 10, 7, 12, 2, 1, 0, 1234, 2233, 33, 1, 2, 3, 4, 0]
    print("简单选择排序：", choose_sort(arr))
