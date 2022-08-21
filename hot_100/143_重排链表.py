# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reorder-list/
解题思路：解法1：将链表元素存储到数组中，然后找到链表中间的结点，按照规则拼接即可。这样时间复杂度是 O(n)，空间复杂度是 O(n)。
        解法2：找到中间节点，将中间节点后半部分链表作反转，随后按规则重排链表即可。寻找链表中间节点可以通过快慢指针slow=head,
              fast=head.next.next.fast到达末尾，slow刚好处于中间节点，不需要区分链表长度为奇偶。反转链表可参考lc_206.
              时间复杂度是 O(n)，空间复杂度是 O(1)。


"""

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

    def reorderList1(self, head: ListNode):  # 解法1  数组
        if not head: return
        array = list()
        node = head           # 注意不要直接循环head
        while node:
            array.append(node)
            node = node.next
        i = 0
        j = len(array) - 1
        while i < j:
            array[i].next = array[j]
            i += 1
            if i == j: break
            array[j].next = array[i]
            j -= 1
        array[j].next = None
        return head      # 在lc中不需要返回值，在本地测试的时候需要

    def _rever_list(self, head: ListNode) -> ListNode:
        if not head:return None
        pre, next = None, None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reorderList2(self, head: ListNode) -> None:  # 解法2
        if not head: return
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next      # 找到链表中间节点
        mid = slow
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self._rever_list(l2)   # 链表后半段反转
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l1 = l1_next

            l2.next = l1
            l2 = l2_next
        return head



if __name__ == "__main__":
    s = Solution()
    head = s.test_case()
    res_head = s.reorderList2(head)
    out = list()
    while res_head:
        out.append(res_head.val)
        res_head = res_head.next
    print(out)
