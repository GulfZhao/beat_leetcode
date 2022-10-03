# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/linked-list-cycle-ii/
题目难度：medium
解题思路: 哈希表：使用哈希表来存储所有已经访问过的节点。每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，且该节点为
         环形链表的第一个节点。
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

    def detectCycle(self, head: [ListNode]) -> [ListNode]:
        if not head: return None
        hash_set = set()
        while head:
            if head not in hash_set:
                hash_set.add(head)
                head = head.next
            else:
                return head
        return None


# 测试用例
if __name__ == "__main__":
    s = Solution()
    head = s.test_case()
    print(s.detectCycle(head))
