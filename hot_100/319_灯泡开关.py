# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/bulb-switcher/
解题思路：对于第k个灯泡被切换的次数恰好就是其约数的个数，而第k个灯泡若为点亮状态则需要其约数的个数为奇数。故首先需要求解1-n范围内所有数的约数，
        然后筛选出约数个数为奇数的数量，该数量则表明n轮后，灯泡亮的数目。而约数个数为奇数则需要k是完全平方数，即x平方=k
"""
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(float(n)))


if __name__ == "__main__":
    s = Solution()
    print(s.bulbSwitch(10))
