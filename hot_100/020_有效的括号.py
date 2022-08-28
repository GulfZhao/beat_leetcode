# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/valid-parentheses/
解题思路: 哈希表存储括号对应关系即{"(":")"},此外判断括号有效性的过程可以利用栈，遇到左括号入栈，遇到右括号，判断与栈顶元素是否匹配，匹配则出栈，
        相反则直接输出false，最后通过判断栈是否为空，可以判断字符串是否有效
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stack = list()
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack


if __name__ == "__main__":
    s = Solution()
    test = "()[]{}"
    res = s.isValid(test)
    print(res)