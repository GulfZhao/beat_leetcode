# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/two-sum/
解题思路: num1+num2=target,核心是要要num2=target-num1是否在list中，通过字典来模拟哈希查找（时间复杂度为O(1)）
字典描述：{元素值：元素下标}，如{2：1}
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha = dict()
        for i in range(len(nums)):
            if target-nums[i] in ha:
                return [ha[target-nums[i]], i]
            ha[nums[i]] = i


if __name__ == "__main__":
    s = Solution()
    res = s.twoSum([2, 7, 11, 15], 18)
    print(res)
