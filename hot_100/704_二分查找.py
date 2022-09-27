# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/binary-search/submissions/
题目难度：easy
解题思路: 经典二分查找
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    s = Solution()
    test_data = [-1, 0, 3, 5, 9, 12]
    res = s.search(test_data, 5)
    print(res)
