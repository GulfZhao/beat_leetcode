# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/next-permutation/?favorite=2cktkvj
题目难度：medium
解题思路: 下一个排列”的定义是：给定数字序列的字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）,
        如数字序列【1，2，3】，对应123，123下一个数字即132，故下个序列即[1,3,2].第一步：在 nums[i] 中找到 i 使得 nums[i] < nums[i+1]，
        此时较小数为 nums[i]，并且 [i+1, n) 一定为下降区间。第二步：如果找到了这样的 i ，则在下降区间 [i+1, n) 中从后往前找到第一个 j ，
        使得 nums[i] < nums[j] ，此时较大数为 nums[j]。第三步，交换 nums[i] 和 nums[j]，此时区间 [i+1, n) 一定为降序区间。
        最后原地交换 [i+1, n) 区间内的元素，使其变为升序，无需对该区间进行排序。
"""


class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # 查找第一个相邻升序的元素对
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:  #
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:  # 必定为降序，不需要重排，只需要位置呼唤即可
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = Solution()
    test = [3, 2, 1, 4]
    s.nextPermutation(test)
    print(test)
