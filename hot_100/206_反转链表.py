# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reverse-linked-list/
解题思路: 3个指针，pre，cur,next,循环移动cur，直到cur为none.
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

    def reverseList(self, head: [ListNode]) -> [ListNode]:
        if not head: return None
        pre = next = None
        cur = head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


# 测试用例
if __name__ == "__main__":
    s = Solution()
    head = s.test_case()
    res_head = s.reverseList(head)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
