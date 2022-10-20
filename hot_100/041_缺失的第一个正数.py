# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/first-missing-positive/
题目难度：hard
解题思路: 原地哈希，将原有数组当作哈希表。核心突破点在于长度为N的数组，其没有出现的最小的正整数一定在[1,N+1]中。共分为两个阶段：
         第一阶段：元素置换，遍历所有元素将属于[1,N]的x放在其正确的位置num[x-1]
         第二阶段：再次遍历，寻找第一个位置缺失的元素并返回
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):  # 阶段1:位置交换
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:  # 处于索引范围内且所处的位置错误则进行交换
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):  # 阶段2:寻找第一个位置缺失的元素并返回
            if nums[i] != i + 1:
                return i + 1
        return n + 1  # 若不在【1，N】范围内，则缺失的最小正整数则为n+1


if __name__ == "__main__":
    s = Solution()
    test_data = [4, 2, -1, 3]
    res = s.firstMissingPositive(test_data)
    print(res)
