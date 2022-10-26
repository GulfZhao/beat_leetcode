# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reverse-linked-list/
题目难度：easy
解题思路: 3个指针，pre，cur,next,循环移动cur，直到cur为none.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def generate_listNode(self, queue):
        n = len(queue)
        if n == 0: return None
        node_list = []
        for value in queue:
            node_list.append(ListNode(value))
        i = 0
        while i + 1 < n:
            node_list[i].next = node_list[i + 1]
            i += 1
        node_list[n - 1].next = None
        return node_list[0]

    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head: return None
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre


# 测试用例
if __name__ == "__main__":
    s = Solution()
    queue = [1, 2, 3, 4, 5]
    head = s.generate_listNode(queue)
    res_head = s.reverseList(head)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
