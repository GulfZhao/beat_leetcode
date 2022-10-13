# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-increasing-subsequence/
题目难度：medium
解题思路：子序列（subsequence）：子序列并不要求连续，例如：序列 [4, 6, 5] 是 [1, 2, 4, 3, 7, 6, 5] 的一个子序列,而子串则需要连续，这个
        需要特别区分。方法：动态规划+二分查找
"""


class Solution:

    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num
            if j == res: res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    test_data = [10, 9, 2, 5, 3, 7, 101, 18]
    out = s.lengthOfLIS(test_data)
    print(out)
