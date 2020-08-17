# 快速排序
# 从序列中选一个数作为比较标准， 比它小的放在一边，比它大的放在一边，在两个集合序列中再次使用快排的方法进行排序

def quick_sot(arr):
    if len(arr) >= 2:

        key = arr[len(arr) // 2]

        arr.remove(key)
        big = []
        small = []
        for i in range(len(arr)):
            if arr[i] >= key:
                big.append(arr[i])
            else:
                small.append(arr[i])
        return quick_sot(small) + [key] + quick_sot(big)
    else:
        return arr


if __name__ == '__main__':
    arr = [1, 23, 5, 3, 555, 2, 10]
    print(quick_sot(arr))
