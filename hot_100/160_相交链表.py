# -*- coding: UTF-8 -*-
"""
题目链接:https://leetcode.cn/problems/intersection-of-two-linked-lists/
解题思路: 给定的 2 个链表的长度如果一样长，都从头往后扫即可。如果不一样长，需要先“拼成”一样长。把 B 拼接到 A 后面，把 A 拼接到 B 后面。
        这样 2 个链表的长度都是 A + B。再依次扫描比较 2 个链表的结点是否相同。
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if not pa:
                pa = headB
            else:
                pa = pa.next
            if not pb:
                pb = headA
            else:
                pb = pb.next

        return pa


# 测试用例
if __name__ == "__main__":
    pass