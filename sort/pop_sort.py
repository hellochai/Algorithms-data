# 冒泡排序
# 依次比较相邻元素

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == '__main__':
    arr = [1,23,5,3,555,2,10]
    print(bubble_sort(arr))
