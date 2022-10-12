# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/implement-queue-using-stacks/
题目难度：easy
解题思路: 一个栈用于存储push数据，一个栈用于pop。当stack2为空时，将stack1的数据全部压入stack2再pop
"""


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)

