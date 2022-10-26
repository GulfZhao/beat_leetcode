# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
题目难度：medium
解题思路:利用快慢指针，快慢指针相差n，当快指针指到链表末尾时，慢指针的next刚好是待删除的指针。
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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dumpy = ListNode(0, head)  # 哑节点，用于指向链表的头节点
        slow = dumpy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dumpy.next


# 测试用例
if __name__ == "__main__":
    s = Solution()
    queue = [1, 2, 3, 4, 5]
    head = s.generate_listNode(queue)
    res_head = s.removeNthFromEnd(head, 2)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
