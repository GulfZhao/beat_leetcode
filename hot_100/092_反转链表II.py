# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reverse-linked-list-ii/
题目难度：medium
解题思路:
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def test_case(self):
        node5 = ListNode(5, None)
        node4 = ListNode(4, node5)
        node3 = ListNode(3, node4)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        return node1

    def reverseBetween(self, head: [ListNode], left: int, right: int) -> [ListNode]:
        if not head: return []
        if left == right: return head
        dumpy_node = ListNode(-1)
        dumpy_node.next = head
        count = 0
        dumpy = dumpy_node

        def reverse(head: ListNode):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        while dumpy:
            if count == left - 1:  # 找到左边界的前一个节点
                pre_left = dumpy
            if count == right:
                right = dumpy
                break
            dumpy = dumpy.next
            count += 1
        left = pre_left.next
        post_right = right.next
        # 切断链接，成为子链表
        pre_left.next = None
        right.next = None
        reverse(left)  # 反转截取的子链表
        pre_left.next = right  # 链表重新相接
        left.next = post_right
        return dumpy_node.next


# 测试用例
if __name__ == "__main__":
    s = Solution()
    head = s.test_case()
    res_head = s.reverseBetween(head, 3, 5)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
