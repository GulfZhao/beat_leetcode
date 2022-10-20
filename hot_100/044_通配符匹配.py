# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/wildcard-matching/
题目难度：hard
解题思路: 画棋盘，二维dp问题
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        row = len(p) + 1
        col = len(s) + 1
        dp = [[False]*col for _ in range(row)]  # 初始化二维dp
        dp[0][0] = True  # s和p都为空时
        for r in range(1, row):
            if p[r-1] == "*" and True in dp[r-1]:
                idx = dp[r-1].index(True)
                dp[r][idx:] = [True] * (col - idx)  # 出现*的当前行,从上一行出现True的列之后都为True
            else:
                for c in range(1, col):  # 遍历s
                    if p[r-1] == "?":    # 如果为？，行值取当前行，列取上一行中出现true的列
                        if dp[r-1][c-1]:
                            dp[r][c] = True
                    else:
                        if p[r-1] == s[c-1]:  # 如果为字符匹配，行值取当前行，列取上一行中出现true的列
                            if dp[r-1][c-1]:
                                dp[r][c] = True
        return dp[row-1][col-1]  # 返回最后一行最后一列的值，若为true则匹配成功，相反则匹配失败


if __name__ == "__main__":
    s = Solution()
    st = "adceb"
    p = "a*b"
    res = s.isMatch(st, p)
    print(res)
