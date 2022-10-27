# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
题目难度：easy
解题思路: 设置哑节点
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

    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if not head: return
        dumpy = ListNode(None, head)
        pre = dumpy
        cur = head
        while cur:
            if pre.val == cur.val:
                next = cur.next
                pre.next = next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next
        return dumpy.next


if __name__ == "__main__":
    s = Solution()
    queue = [0, 0, 0]
    head = s.generate_listNode(queue)
    res = s.deleteDuplicates(head)
    out = []
    while res:
        out.append(res.val)
        res = res.next
    print(out)
