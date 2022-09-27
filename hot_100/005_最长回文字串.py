# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/longest-palindromic-substring/
题目难度：medium
解题思路: 中心扩散法，判断回文核心是找到回文中心，围绕回文中心向两边扩散，扩散的过程判断两边字符是否相等。在遍历过程中，需要考虑到回文字符串的长度
         奇数和偶数两种情况，
"""


class Solution:
    def palindrome(self, s, left, right):
        #寻找回文串
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 返回回文串,list的分片属于前闭后开
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ''
        if len(s) < 2:
            return s
        for i in range(len(s)):
            # 奇数情况下的回文子串
            res_1 = self.palindrome(s, i, i)
            # 偶数情况下的回文子串
            res_2 = self.palindrome(s, i, i+1)
            res = res_1 if len(res_1) > len(res) else res
            res = res_2 if len(res_2) > len(res) else res
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test_data = "cbbd"
    res = s.longestPalindrome(test_data)
    print(res)
