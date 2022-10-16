# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/merge-sorted-array/
题目难度: easy
解题思路: 逆向双指针，为了避免排序过程中覆盖原有数据
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            elif nums1[p1] < nums2[p2]:
                nums1[tail] = nums2[p2]
                p2 -= 1
            else:
                nums1[tail] = nums1[p1]
                p1 -= 1
            tail -= 1


if __name__ == "__main__":
    s = Solution()
    nums1 = [0, 0, 0]
    nums2 = [1, 2, 3]
    m = 0
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
