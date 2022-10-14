# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-increasing-subsequence/
题目难度：medium
解题思路：子序列（subsequence）：子序列并不要求连续，例如：序列 [4, 6, 5] 是 [1, 2, 4, 3, 7, 6, 5] 的一个子序列,而子串则需要连续，这个
        需要特别区分。方法：动态规划.dp[i]表示以nums[i]结尾的最长子序列的长度，转移方程dp[i]=max(dp[i],dp[j]+1)
"""


class Solution:

    def lengthOfLIS(self, nums: [int]) -> int:   # 时间复杂度为O(n^2),空间复杂度为O(n)
        dp = [1] * len(nums)       # 初始化dp
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:   # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    test_data = [10, 9, 2, 5, 3, 7, 101, 18]
    out = s.lengthOfLIS(test_data)
    print(out)
