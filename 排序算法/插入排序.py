# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：稳定排序：时间复杂度O(n^2),空间复杂度O(1)
思路：构建有序序列，从无序序列中选出元素，从后向前依次比较有序序列元素，若已排序元素大于新元素，则向后移动
    若已排序元素小于等于新元素，则插入新元素，重复上述步骤
"""


def InsertSort(arr: List[int]):
    n = len(arr)
    for i in range(1, n):  # 起始arr[0]为已排序,外循环为未排序序列
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # 内循环为比较已排序序列，若小于已排序序列，则后移
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = InsertSort(test_data)
    print(sorted_arr)
