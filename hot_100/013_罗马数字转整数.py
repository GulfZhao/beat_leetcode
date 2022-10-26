# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/roman-to-integer/
题目难度：easy
解题思路: 直接模拟法，需要注意小的数字可能在大的数字左侧，如XL,则需要将小的数字减去，否则易出错
"""


class Solution:

    int_roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def romanToInt(self, s: str) -> int:
        res = 0
        pre = 0
        for st in s:  # 外循环为字符串
            for value, symbol in Solution.int_roman_map:
                if st == symbol:
                    if pre < value:
                        res += value - 2*pre  # 注意减去2*pre
                    else:
                        res += value
                    pre = value
                else:
                    continue
        return res


if __name__ == "__main__":
    s = Solution()
    data = "MCMXCIV"
    res = s.romanToInt(data)
    print(res)
