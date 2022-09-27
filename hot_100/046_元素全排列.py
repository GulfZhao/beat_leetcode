# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/permutations/
题目难度：medium
解题思路: 回溯算法：自后向前追溯曾经访问过的路径，就叫做回溯。构造回溯决策树，通过dfs遍历所有可能的组合。
"""
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):  # 深度优先遍历 depth：记录树的深度，path记录遍历的路径，used：记录该位置是否被使用，res：最终返回结果集
            if depth == size:        # 当depth与size相等，到达叶子节点，记录遍历路径，终止本次深度遍历
                res.append(path[:])
                return
            for i in range(size):        # 遍历第i位到第size位所有组合
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False    # 回溯操作
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test= [1, 2, 3, 4]
    res = s.permute(test)
    print(res)
