# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/intersection-of-two-arrays/
题目难度：easy
解题思路：解法1：暴力解法。
        解法2：希集合存储元素，则可以在 O(1)O(1) 的时间内判断一个元素是否在集合中，从而降低时间复杂度。首先使用两个集合分别存储两个数组中的元素，
        然后遍历较小的集合，判断其中的每个元素是否在另一个集合中，如果元素也在另一个集合中，则将该元素添加到返回值。该方法的时间复杂度可以降低到
         O(m+n)

"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:  # 暴力解法，时间复杂度为O(mn)
        res =set()
        if not nums1 or not nums2: return []
        for val in set(nums1):
            if val in set(nums2):
                res.add(val)
        return list(res)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) > len(set2):
            return [x for x in set2 if x in set1]
        else:
            return [x for x in set1 if x in set2]


# 测试用例
if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    res = s.intersection2(nums1, nums2)
    print(res)
