# -*- coding: UTF-8 -*-
"""
题目链接:https://leetcode.cn/problems/intersection-of-two-linked-lists/
题目难度：easy
解题思路: 双指针法：给定的 2 个链表的长度如果一样长，都从头往后扫即可。如果不一样长，需要先“拼成”一样长。把 B 拼接到 A 后面，把 A 拼接到 B 后面。
        这样 2 个链表的长度都是 A + B。再依次扫描比较 2 个链表的结点是否相同。哈希表：遍历其中一个链表将所有节点存入哈希表中，第二步遍历另外
        链表，第一次出现的元素则为第一个相交点
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> [ListNode]:
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            if not pa:
                pa = headB
            else:
                pa = pa.next
            if not pb:
                pb = headA
            else:
                pb = pb.next

        return pa

    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> [ListNode]:  # 解法2，哈希表，符合easy难度
        if not headA or not headB: return None
        store_dict = set()
        while headA:
            store_dict.add(headA)
            headA = headA.next
        while headB:
            if headB in store_dict:
                return headB
            else:
                headB = headB.next
        return None


# 测试用例
if __name__ == "__main__":
    pass