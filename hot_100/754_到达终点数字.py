# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/reach-a-number/
题目难度：medium
解题思路: 题意与求AB距离最优走法类似，问题可以抽象为给定一个数组为1,2,3,4,5.......i，
         为数组元素添加正负号（正号表示向右跳，负号表示向左跳），使得其和为target的最小数组长度。设p为正数之后，q为负数之和，
         满足p+q=s，p-q=target。s-target=2q>=0,s=i*(i+1)/2,因此就是求最小的i， 使得 i *(i + 1) /2 - target为偶数且大于等于0
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        i = 1
        while True:
            s = i * (i + 1) >> 1
            if s >= target and (s - target) % 2 == 0:
                return i
            i = i + 1


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test = 11
    res = s.reachNumber(test)
    print("result: %d " % res)
