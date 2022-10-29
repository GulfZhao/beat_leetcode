# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/
题目难度：hard
解题思路: 合并k个有序链表，可以选择两两合并的方式
"""


# Definition for singly-linked list.
from typing import List


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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        if left == right:   # 递归结束条件：链表数为1
            return lists[left]
        mid = left + (right - left) // 2       # 将所有链表一分为二
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# 测试用例
if __name__ == "__main__":
    s = Solution()
    input = [[1, 4, 5], [1, 3, 4], [2, 6]]
    node_list = [s.generate_listNode(k) for k in input]
    res_head = s.mergeKLists(node_list)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
