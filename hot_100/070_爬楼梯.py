# -*- coding: UTF-8 -*-
"""
题目链接:https://leetcode.cn/problems/climbing-stairs/
题目难度：easy
解题思路: 青蛙跳台阶问题,斐波那契数列,转换为动态规划dp[i] = dp[i-1] + dp[i-2]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print("please input:")
    data = int(input())
    res = s.climbStairs(data)
    print(res)
