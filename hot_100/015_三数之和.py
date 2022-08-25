# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/3sum/
解题思路: 排序+双指针移动
"""
from typing import List


# 主代码

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        res = list()
        sorted_nums = sort(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] > 0: break
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: continue
            left = i + 1
            right = len(sorted_nums) - 1
            while left < right:
                sums = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if sums == 0:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    while left < right and sorted_nums[left] == sorted_nums[left + 1]: left = left + 1
                    while left < right and sorted_nums[right] == sorted_nums[right - 1]: right = right - 1
                    left = left + 1
                    right = right - 1
                elif sums < 0:
                    left += 1
                else:
                    right = right - 1
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(res)
