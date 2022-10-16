# -*- coding: UTF-8 -*-
"""
题目链接: https://zhuanlan.zhihu.com/p/389541481
题目难度：medium
解题思路: 题目内容：将中文数字的表示方式转化为阿拉伯数字的表示方式
"""


class Solution:

    def cnToArab(self, s: str) -> int:
            common_used_numerals = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7,
                                    '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}

            # Parameters
            cur_total = 0
            unit = 1  # 个（默认）、十、百、千、万

            for i in range(len(s) - 1, -1, -1):
                num = common_used_numerals.get(s[i])

                # 0-9
                if num < 10:
                    cur_total = cur_total + unit * num
                # Special：10 - 19 (十九)
                if num >= 10 and i == 0:
                    unit = num
                    cur_total = cur_total + unit
                # >=20 (二十)
                elif num >= 10:
                    if num > unit:  # 百 十 （进位）
                        unit = num
                    else:  # 三 百 (不进位，算总值)
                        cur_total = cur_total + num * unit

            return cur_total


if __name__ == "__main__":
    s = Solution()
    data = "八十"
    res = s.cnToArab(data)
    print(res)
