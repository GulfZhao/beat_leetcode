# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/add-two-numbers/
解题思路: 需要考虑两个链表不等长和进位的情况，进位需要额外记录下来
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = p = ListNode()  # 初始化一个虚拟头节点，res 作为返回，p 用遍历
        s = 0  # s用作记录进位
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next


# 测试用例
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    res = s.addTwoNumbers(l1,l2)
    out = list()
    while res:
        out.append(res.val)
        res = res.next if res else None
    print(out)
