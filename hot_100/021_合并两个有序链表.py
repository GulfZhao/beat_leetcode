# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/merge-two-sorted-lists/
题目难度：easy
解题思路: 将两个升序链表合并为一个新的升序链表，迭代
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

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:   # 迭代
        if not list1: return list2
        if not list2: return list1
        dummy_head = ListNode()
        p1, p2 = list1, list2
        pre = dummy_head        # 不能忽略
        while p1 and p2:
            if p1.val > p2.val:
                pre.next = p2
                p2 = p2.next
            else:
                pre.next = p1
                p1 = p1.next
            pre = pre.next
        if not p1: pre.next = p2
        if not p2: pre.next = p1
        return dummy_head.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:  # 递归
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 测试用例
if __name__ == "__main__":
    s = Solution()
    queue1 = [1, 2, 4]
    queue2 = [1, 3, 4]
    l1 = s.generate_listNode(queue1)
    l2 = s.generate_listNode(queue2)
    res_head = s.mergeTwoLists(l1, l2)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
