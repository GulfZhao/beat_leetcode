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

    def generate_tree(self, queues):
        n = len(queues)
        if n == 0: return None
        treeNode_list = []
        for value in queues:
            if value:
                node = TreeNode(value)
            else:
                node = None
            treeNode_list.append(node)  # 生成treeNode
        i = 0
        while 2 * i + 2 < n:
            if treeNode_list[i]:
                treeNode_list[i].left = treeNode_list[2 * i + 1]
                treeNode_list[i].right = treeNode_list[2 * i + 2]
            i += 1
        return treeNode_list[0]

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
    data = [1, 2, 3, None, 5, None, 4]
    root = s.generate_tree(data)
    res = s.levelOrder(root)
    print(res)
