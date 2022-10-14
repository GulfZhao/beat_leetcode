# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/perfect-squares/
题目难度： medium
解题思路: 动态规划求最优解，dp[i]表示到数字i组成最少完全平方个数,背包问题。
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]  # 初始化，最坏的情况就是i个1的组合，dp[i]表示以i为和的完全平方数的最少数量
        for i in range(1, n):  # 遍历物品，即可以作为组合的平方数
            if i * i > n: break
            num = i * i  # 物品
            for j in range(num, n + 1):  # 遍历背包，前闭后开，故需要n+1
                dp[j] = min(dp[j], dp[j - num] + 1)
        return dp[n]


# 测试用例
if __name__ == "__main__":
    s = Solution()
    print("please input data:")
    test_data = input()
    out = s.numSquares(int(test_data))
    print(out)
