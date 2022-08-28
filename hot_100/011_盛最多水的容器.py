# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/container-with-most-water/
解题思路: 利用双指针分别指向数组边界，计算容积面积
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            ans = max(area, ans)
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
        return ans


if __name__ == "__main__":
    s = Solution()
    test = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    res = s.maxArea(test)
    print(res)
