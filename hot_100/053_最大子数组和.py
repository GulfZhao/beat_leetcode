# -*- coding: UTF-8 -*-
"""
题目链接:https://leetcode.cn/problems/maximum-subarray/
题目难度：medium
解题思路: 动态规划问题：只需要找到最优解，不需要给出具体的方案。给出动态规划方程dp[i]:表示以nums[i]结尾的连续子数组的最大和
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  # 解法1：dp
        if len(nums) == 0: return 0

        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] > 0:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    test = [5, 4, -1, 7, 8]
    res = s.maxSubArray(test)
    print(res)
