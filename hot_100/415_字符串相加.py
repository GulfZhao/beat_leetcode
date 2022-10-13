# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/add-strings/
题目难度：easy
解题思路: 双指针分别指向num1,num2,模拟人工加法，注意记录进位
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0  # 进位
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0  # 考虑到num1，num2长度不一情况，通过补0来补齐位数
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        res = "1" + res if carry else res
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    num1, num2 = "123", "11"
    out = s.addStrings(num1, num2)
    print(out)
