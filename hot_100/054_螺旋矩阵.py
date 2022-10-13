# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/spiral-matrix/
题目难度：medium
解题思路: 每次取第一行，然后旋转矩阵，直到取完所有行
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            # 削头（第一层）
            res += matrix.pop(0)
            # 将剩下的逆时针转九十度，等待下次被削
            matrix = list(zip(*matrix))[::-1]  # [::-1]实现列表倒序，zip(*matrix) 为zip(matrix)逆操作
        return res


if __name__ == "__main__":
    s = Solution()
    test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = s.spiralOrder(test)
    print(res)
