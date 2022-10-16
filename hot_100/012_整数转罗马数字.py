# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/integer-to-roman/
题目难度：medium
解题思路: 直接模拟法，题目中规定nums<4000,可采用直接模拟法，从最大单位开始（1000），当前数值 不超过 num，则从num 中不断减去value，
直至num 小于value，然后遍历下一个数值-符号对
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

    def intToRoman(self, num: int) -> str:
        roman = list()
        for value, symbol in Solution.int_roman_map:
            while num >= value:
                num -= value
                roman.append(symbol)
            if num == 0:
                break
        return "".join(roman)


if __name__ == "__main__":
    s = Solution()
    data = 345
    res = s.intToRoman(data)
    print(res)
