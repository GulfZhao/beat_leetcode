# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：不稳定排序：时间复杂度O(nlogn),空间复杂度O(1)
思路：希尔排序也称递减增量排序算法，是插入排序的一种更高效的改进版本，核心思想是希尔排序是把记录按下标的一定增量分组，
     对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
"""


def ShellSort(arr: List[int]):
    n = len(arr)
    gap = n // 2         # 分组
    while gap > 0:        # 终止条件为gap == 1
        for i in range(gap, n):   # 插入排序思路，区别在于步长由1改为gap
            key = arr[i]
            j = i - gap
            while j >= 0 and key < arr[j]:
                arr[j+gap] = arr[j]
                j = j - gap
            arr[j+gap] = key
        gap = gap // 2    # 减小分组数
    return arr


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = ShellSort(test_data)
    print(sorted_arr)
