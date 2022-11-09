# -*- coding: UTF-8 -*-
from typing import List

"""
注意：默认为升序
特性：不稳定排序：时间复杂度O(nlogn),空间复杂度O(1)
思路：堆是一种数据结构，分为小根堆（根节点小于孩子节点），大根堆（根节点大于孩子节点），升序用大根堆，降序用小根堆.堆总是一棵完全二叉树
    根据队列，可以画出树形图，升序排序，则需要将构造大根堆，
"""


def HeapSort(arr: List[int]):
    def shift_down(arr, n, parent):  # 构造堆
        largest = parent
        left = 2 * parent + 1
        right = 2 * parent + 2
        if left < n and arr[largest] < arr[left]:  # 最大堆为小于，最小堆为大于
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != parent:
            arr[largest], arr[parent] = arr[parent], arr[largest]
            shift_down(arr, n, largest)  # 堆结构可能被破坏，需要重新再调整

    n = len(arr)
    for i in range(n-1, -1, -1):  # 创建最大堆
        shift_down(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 堆顶点与最后一位元素交换位置
        shift_down(arr, i, 0)   # 堆调整

    return arr


if __name__ == "__main__":
    test_data = [3, 5, 7, 1, 34, 24, 8, 21]
    sorted_arr = HeapSort(test_data)
    print(sorted_arr)
