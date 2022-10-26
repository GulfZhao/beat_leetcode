# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/palindrome-linked-list/solution/
题目难度：easy
解题思路: 找到中间节点，将链表一分为二，后半部分反转链表，依次从头开始遍历两个子链表，若出现不同返回false，相反返回true
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

    def isPalindrome(self, head: [ListNode]) -> bool:
        def reverse(head):
            pre = None
            cur = head
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        l1 = head
        l2 = mid.next
        l2 = reverse(l2)
        while l1 and l2:
            if l1.val == l2.val:
                l1 = l1.next
                l2 = l2.next
            else:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    queue = [1, 2, 2, 1]
    head = s.generate_listNode(queue)
    res = s.isPalindrome(head)
    print(res)
