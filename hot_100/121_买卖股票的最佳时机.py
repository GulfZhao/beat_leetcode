# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
解题思路:一次遍历，记录最小值，并计算price[i]与最小值的差值得出收益，取最大收益即最大利润
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        max_profit = 0
        for price in prices:
            minprice = min(minprice, price)
            if price > minprice:
                max_profit = max(max_profit, price-minprice)
        return max_profit


if __name__ == "__main__":
    s = Solution()
    test = [7, 1, 5, 3, 6, 4]
    res = s.maxProfit(test)
    print(res)
