# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-common-subsequence/
题目难度：medium
解题思路：求两个字符串的最长公共子序列，最长马上联想到动态规划，而由于涉及两个字符串故是典型的二维动态规划问题。dp[i][j]表示字符串text1[0:i],
        text2[0:j]的最长公共子序列
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m + 1)]   # 创建m+1行，n+1列二维矩阵。边界：当i=0或j=0，dp[i][j]=0，初始化必须用for_range
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:          # 状态转移方程，存在公共字符串，则有dp[i][j] = dp[i-1][j-1] + 1
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 字符串不相等，则要考虑两种情况下当最长公共子序列长度，求最大值
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    out = s.longestCommonSubsequence(text1, text2)
    print(out)
