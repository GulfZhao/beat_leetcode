# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/combination-sum/
题目难度：medium
解题思路: 求所有组合数->回溯算法，dfs，元素重复情况需要考虑剪枝，我们在搜索的时候就需要按某种顺序搜索。具体的做法是：
每一次搜索的时候设置 下一轮搜索的起点 begin.即从每一层的第 2个结点开始，都不能再搜索产生同一层结点已经使用过的 candidate 里的元素
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target < 0:   # 终止条件，若为负数，则没有满足的组合
                return
            if target == 0:  # 终止条件，满足和为target，加入到结果集中
                res.append(path)
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


if __name__ == "__main__":
    s = Solution()
    test = [2, 3, 6, 7]
    res = s.combinationSum(test, 7)
    print(res)
