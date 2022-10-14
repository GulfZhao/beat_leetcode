# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/coin-change/
题目难度： medium
解题思路: 动态规划求最优解，dp[i]表示到数字i需要最少的零钱数
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


# 测试用例
if __name__ == "__main__":
    s = Solution()
    coin = [1, 2, 5]
    amount = 11
    out = s.coinChange(coin, amount)
    print(out)
