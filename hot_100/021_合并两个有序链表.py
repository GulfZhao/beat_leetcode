# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/merge-two-sorted-lists/
解题思路: 将两个升序链表合并为一个新的升序链表，迭代
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def test_case(self):
        node6 = ListNode(6, None)
        node5 = ListNode(5, None)
        node4 = ListNode(4, node6)
        node3 = ListNode(3, node5)
        node2 = ListNode(2, node4)
        node1 = ListNode(1, node3)
        return node1, node2

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1: return list2
        if not list2: return list1
        dummy_head = ListNode()
        p1, p2 = list1, list2
        pre = dummy_head
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


# 测试用例
if __name__ == "__main__":
    s = Solution()
    l1, l2 = s.test_case()
    res_head = s.mergeTwoLists(l1, l2)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
