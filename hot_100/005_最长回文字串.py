# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-palindromic-substring/
解题思路: 动态规划
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[1] * length for _ in range(length)]
        left, right = 0, 0 #长度为1时
        for i in range(1, length):
             for j in range(length-i):
                if s[j] == s[j+i] and dp[j+1][j+i-1]:
                    dp[j][j+i] = 1
                    left, right = j, j+i
                else:
                    dp[j][j+i] = 0
        return s[left: right+1]


# 测试用例
if __name__ == "__main__":
    s = Solution()
    res = s.longestPalindrome('baba')
    print(res)
