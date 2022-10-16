# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/binary-tree-right-side-view/
题目难度：medium
解题思路: 取树的每层的最右侧节点，通过层序遍历来获取每层的节点，将每层的最右侧节点值加入到返回结果中，输出最终结果
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

    def rightSideView(self, root: [TreeNode]) -> List[int]:
        if not root: return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            nex = []
            for node in queue:
                tmp.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            res.append(tmp[-1])
            queue = nex
        return res


if __name__ == "__main__":
    s = Solution()
    data = [1, 2, 3, None, 5, None, 4]
    root = s.generate_tree(data)
    out = s.rightSideView(root)
    print(out)
