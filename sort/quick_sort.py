# 快速排序

"""
    从序列中选一个数作为比较标准， 比它小的放在一边，比它大的放在一边，在两个集合序列中再次使用快排的方法进行排序
    时间复杂度:
        最好情况(每次总是选到最小或最大元素作划分元)
         T(n)=O(nlog2n)
        最坏情况(每次总是选到最小或者最大元素作为划分元)
          T(n) = O(n^2)

    空间复杂度: 需栈空间以实现递归
        最坏: S(n)=O(n)
        一般情况: S(n)=O(log2n)
"""

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
