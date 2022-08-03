# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-substring-without-repeating-characters/
解题思路: 滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字符，就需要缩小左边界，直到重复的字符移出了左边界，
然后继续移动滑动窗口的右边界。以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = list()
        max_len = 0
        for st in s:
            if st not in res:
                res.append(st)
            else:
                index = res.index(st)
                while index >= 0:
                    res.pop(index)
                    index = index - 1
                res.append(st)
            max_len = len(res) if len(res) > max_len else max_len
        return max_len


# 测试用例
if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring('abcabcbb')
    print(res)
