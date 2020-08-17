from typing import List


def getSum(n):
    sum = 0
    sum += n

    print(sum)


def getL(arr, key):
    if key < min(arr):
        return False


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dict = {}
        for i in range(1, target + 1):
            dict[i] = []

        for i in range(1, target + 1):
            for j in candidates:
                if i == j:
                    dict[i].append([i])
                elif i > j:
                    for k in dict[i - j]:
                        x = k[:]
                        x.append(j)
                        x.sort()  # 升序，便于后续去重
                        if x not in dict[i]:
                            dict[i].append(x)

                return dict[target]


if __name__ == '__main__':
    getSum(123)
    l = [1, 23, 4, 4, 5, 3, 5]
    s = Solution()
    print(s.combinationSum(l, 8))
