# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/generate-parentheses/?favorite=2cktkvj
题目难度：medium
解题思路: 回溯问题，通过构造一颗隐式的树来求解，一般用深度优先算法。基本过程：
https://leetcode.cn/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        cur_str = ''

        def dfs(cur_str, left, right, n):
            """
            :param cur_str: 从根结点到叶子结点的路径字符串
            :param left:  左括号已使用个数
            :param right: 右括号已使用个数
            :param n: 括号数
            :return:
            """
            if left == n and right == n:
                res.append(cur_str)
                return
            if left < right:
                return
            if left < n:
                dfs(cur_str + '(', left + 1, right, n)
            if right < n:
                dfs(cur_str + ')', left, right + 1, n)

        dfs(cur_str, 0, 0, n)
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.generateParenthesis(3)
    print(res)