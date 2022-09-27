# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/search-in-rotated-sorted-array/
题目难度：medium
解题思路:有序数组经过旋转后将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。有序数组搜索-->二分查找
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right + left) >> 1
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[left]:     # 落在数值较大的区间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[right]:  # 落在数值较小的区间
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:                         # 当数组长度为2时，会出现这种情况
                if nums[mid] == nums[right]:
                    right -= 1
                if nums[mid] == nums[left]:
                    left += 1
        return -1


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test = [4, 5, 6, 7, 0, 1, 2]
    res = s.search(test, 6)
    print(res)
