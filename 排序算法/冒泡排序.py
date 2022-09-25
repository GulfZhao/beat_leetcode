# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：稳定排序：时间复杂度O(n^2),空间复杂度O(1)
思路：比较相邻元素，若第一个比第二个大，交换位置，第一次排序后最大值放在队尾。第二次遍历的时候排除掉已排序
     元素n-i-1，继续重复上面步骤
"""


def bubbleSort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = bubbleSort(test_data)
    print(sorted_arr)
