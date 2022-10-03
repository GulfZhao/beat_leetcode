# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode. cn/problems/lru-cache/
题目难度：medium
解题思路: 实现LRU(最近最少使用)缓存机制，需要实现方法get，put，且时间时间复杂度为O（1），get通过map可以满足。LRU插入和更新的时候发生在链首，
         而删除则发生在链尾，通过双向链表可以实现实现0（1）时间复杂度。故LRU缓存通过哈希表和双向链表来实现
"""


class DLinkNode:                          # 定义双向链表，节点为哈希表
    def __init__(self, key=0, value=0):
        self.value = value
        self.key = key
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = DLinkNode()   # 伪头部
        self.tail = DLinkNode()   # 伪尾部
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        if key not in self.cache:
            node = DLinkNode(key, value)
            self.cache[key] = node      # 添加进哈希表
            self.addToHead(node)        # 添加至双向链表的头部
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()    # 移除双向链表尾部节点
                self.cache.pop(removed.key)    # 移除哈希表
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def removeNode(self, node: DLinkNode):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre

    def removeTail(self):
        pre = self.tail.pre
        self.removeNode(pre)
        return pre

    def addToHead(self, node: DLinkNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def moveToHead(self, node: DLinkNode):
        self.removeNode(node)
        self.addToHead(node)
