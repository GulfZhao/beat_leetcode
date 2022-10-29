# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/letter-combinations-of-a-phone-number/?favorite=2cktkvj
题目难度：medium
解题思路: 所有组合，回溯dfs
"""
from typing import List


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        dig_dict = {
            "2": "abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(conbination,index):
            if index == len(digits):
                res.append(conbination)
                return
            chars = dig_dict[digits[index]]
            for char in chars:
                dfs(conbination+char, index+1)
        if not digits: return []
        res = []
        dfs('', 0)
        return res


if __name__ == "__main__":
    s = Solution()
    data = "23"
    res = s.letterCombinations(data)
    print(res)
