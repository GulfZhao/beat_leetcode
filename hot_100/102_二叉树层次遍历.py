# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/binary-tree-level-order-traversal/
题目难度：medium
解题思路: 层次遍历，逐层遍历，每层节点保存为子数组。利用队列。参考：https://juejin.cn/post/6844903807759941646
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def test_case(self):
        num_4 = TreeNode(4, None, None)
        num_5 = TreeNode(5, None, None)
        num_6 = TreeNode(6, None, None)
        num_7 = TreeNode(7, None, None)
        num_3 = TreeNode(3, num_6, num_7)
        num_2 = TreeNode(2, num_4, num_5)
        root = TreeNode(1, num_2, num_3)
        return root

    def levelOrder(self, root: [TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            tmp = []
            nex = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            queue = nex
            res.append(tmp)
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    root = s.test_case()
    res = s.levelOrder(root)
    print(res)
