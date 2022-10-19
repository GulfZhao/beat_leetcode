# -*- coding: UTF-8 -*-
"""
题目链接:https://leetcode.cn/problems/sqrtx/
题目难度：easy
解题思路: x的平方根的整数部分ans满足 k^2 <= x,找出满足条件的最大k值即可，方法二分查找，最右值
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x
        left, right = 1, x >> 1
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print("please input:")
    data = int(input())
    res = s.mySqrt(data)
    print(res)
