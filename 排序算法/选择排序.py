# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：不稳定排序：时间复杂度O(n^2),空间复杂度O(1)
思路：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
     然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""


def SelectionSort(arr: List[int]):
    n = len(arr)
    for i in range(n-1):
        min = i    # 最小元素索引
        for j in range(i+1, n):      # 遍历未排序元素，记录最小元素的索引
            if arr[j] < arr[min]:
                min = j
        if i != min:   # 交换最小元素
            arr[i], arr[min] = arr[min], arr[i]
    return arr


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = SelectionSort(test_data)
    print(sorted_arr)
