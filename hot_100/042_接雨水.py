# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/trapping-rain-water/?favorite=2cktkvj
题目难度：hard
解题思路: 积水量取决于两侧墙的高度，故需要找到所有可以匹配的墙的组合，min(左墙高度，右墙高度）* （右侧墙下标-左侧墙下标-1），可以利用单调栈。
        入栈原则：当前高度小于等于栈顶高度或栈空，入栈，指针后移。出栈原则：当前高度大于栈顶高度，出栈，计算出当前墙和栈顶的墙之间水的多少，
        然后计算当前的高度和新栈的高度的关系，重复直到当前墙的高度不大于栈顶高度或者栈空，然后把当前墙入栈，指针后移。
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = list()
        ans = 0
        p = 0
        while p < len(height):
            while stack and height[stack[-1]] < height[p]:   # 出栈：当前指针对应当墙高度大于栈顶且栈不为空
                pop_index = height[stack[-1]]   # 记录栈顶高度，
                stack.pop()       # 出栈
                if not stack:     # 栈空跳出将当前指针入栈
                    break
                distance = p - stack[-1] - 1      # 计算两墙之间的距离
                h = min(height[p], height[stack[-1]])      # 木桶效应，取最小值
                ans = ans + distance * (h - pop_index)     # 墙与'地面'的高度差与墙距相乘得出盛水量
            stack.append(p)     # 入栈
            p += 1              # 指针后移
        return ans


if __name__ == "__main__":
    s = Solution()
    test_data = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = s.trap(test_data)
    print(res)
