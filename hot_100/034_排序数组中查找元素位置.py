# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
解题思路: 有序数组寻找目标值->二分查找
"""
from typing import List


class Solution:
    def searchFirst(self, nums, n, target):  # 二分查找第一个与 target 相等的元素，时间复杂度 O(logn)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                if mid == 0 or nums[mid - 1] != target:
                    return mid
                right = mid - 1
        return -1

    def searchLast(self, nums, n, target):  # 二分查找最后一个与 target 相等的元素，时间复杂度 O(logn)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                if mid == n - 1 or nums[mid + 1] != target:
                    return mid
                left = mid + 1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        n = len(nums)
        ret_1 = self.searchFirst(nums, n, target)
        ret_2 = self.searchLast(nums, n, target)
        return [ret_1, ret_2]


if __name__ == "__main__":
    s = Solution()
    test = [5, 7, 7, 8, 8, 10]
    res = s.searchRange(test, 8)
    print(res)
