# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
题目难度：medium
解题思路: 与82的区别在于重复元素都需要删除，留下非重复的元素
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
        dumpy = ListNode(0, head)
        cur = dumpy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
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
