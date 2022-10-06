# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/kth-largest-element-in-an-numsay/
题目难度：medium
解题思路:
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def shift_down(nums, n, parent):  # 构造堆
            largest = parent
            left = 2 * parent + 1
            right = 2 * parent + 2
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != parent:
                nums[largest], nums[parent] = nums[parent], nums[largest]
                shift_down(nums, n, largest)  # 堆结构可能被破坏，需要重新再调整
        n = len(nums)
        for i in range(n, -1, -1):  # 构建最大堆
            shift_down(nums, n, i)
        for i in range(n - 1, n-1-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            shift_down(nums, i, 0)
        print(nums)
        return nums[n-1-(k-1)]


if __name__ == "__main__":
    s = Solution()
    test_data = [3, 2, 1, 5, 6, 4]
    k = 1
    res = s.findKthLargest(test_data, k)
    print(res)
