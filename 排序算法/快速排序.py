# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：不稳定排序：时间复杂度O(nlog(n)),空间复杂度O(log(n))
思路：找队列的基准点，将队列一分为二，小于基准的放前面，大于的放在后面；递归操作
"""


def QuickSort(arr: List[int]):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        grater = [x for x in arr[1:] if x >= pivot]
        return QuickSort(less) + [pivot] + QuickSort(grater)


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = QuickSort(test_data)
    print(sorted_arr)
