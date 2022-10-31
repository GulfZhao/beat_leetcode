# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reverse-nodes-in-k-group/
题目难度：hard
解题思路: 链表节点按照 k 个一组分组，所以可以使用一个指针 head 依次指向每组的头节点。这个指针每次向前移动 k 步，直至链表结尾。
         对于每个分组，我们先判断它的长度是否大于等于 k。若是，我们就翻转这部分链表，否则不需要翻转。
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

    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next
        cur = head
        while pre != tail:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return tail, head

    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        hair = ListNode(0, head)
        pre = hair
        while head:
            tail = pre
            for _ in range(k):  # 查看剩余部分长度是否大于等于 k
                tail = tail.next
                if not tail:
                    return hair.next
            next = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = next
            pre = tail
            head = tail.next
        return hair.next


# 测试用例
if __name__ == "__main__":
    s = Solution()
    queue = [1, 2, 3, 4, 5]
    head = s.generate_listNode(queue)
    res_head = s.reverseKGroup(head, 2)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
