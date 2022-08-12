# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/linked-list-cycle/
解题思路: 快慢指针，若存在环，则快指针必定会追上慢指针；哈希表：使用哈希表来存储所有已经访问过的节点。
每次我们到达一个节点，如果该节点已经存在于哈希表中，则说明该链表是环形链表，否则就将该节点加入哈希表中。重复这一过程，直到我们遍历完整个链表即可。
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

    def hasCycle(self, head:ListNode) -> bool:  # 快慢指针
        if not head: return None
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def hasCycle_2(self, head: ListNode) -> bool:  # 哈希表
        hash_set = set()
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        return False




# 测试用例
if __name__ == "__main__":
    s = Solution()
    head = s.test_case()
    print(s.hasCycle(head))
