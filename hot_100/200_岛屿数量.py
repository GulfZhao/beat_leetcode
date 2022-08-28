# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/number-of-islands/
解题思路: 岛屿问题->网格类，典型解法DFS，参考二叉树dfs,确定循环跳出条件（root==null）以及相邻节点(左子树和右子树)。网格点坐标（r,c),相邻节点为
        上下左右，跳出条件为到达网格边界以及到达grid[i][j]=0，为了避免重复遍历，对遍历过的节点做标记
"""
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0': return  # 跳出条件
            grid[i][j] = '0'     # 标记遍历过的点
            dfs(grid, i - 1, j)  # 相邻节点
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):   # 遍历所有网状节点
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    test = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res = s.numIslands(test)
    print(res)
