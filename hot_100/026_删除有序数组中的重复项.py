# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
题目难度：easy
解题思路: 解法1：pre记录前一个值，比较当前值与pre，若重复则pop，数组长度减1，若不想等，向后移动数组。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        pre = nums[0]
        i = 1
        while i < n:
            if nums[i] == pre:
                nums.pop(i)
                n -= 1
            else:
                pre = nums[i]
                i += 1

        return len(nums)


if __name__ == "__main__":
    s = Solution()
    test = [1, 2, 2, 2, 4, 4, 5, 6]
    res = s.removeDuplicates(test)
    print(res)
