# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/binary-tree-maximum-path-sum/
题目难度: hard
解题思路: 题目解读，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。定义节点的最大贡献值：
        空节点的贡献值为0，非空节点的最大贡献值等于节点值与其子节点中的最大贡献值之和（对于叶节点而言，最大贡献值等于节点值）
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maxSum = 0

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

    def maxPathSum(self, root: [TreeNode]) -> int:
        def maxGain(node):
            if not node: return 0
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            newPathValue = node.val + leftGain + rightGain
            self.maxSum = max(self.maxSum, newPathValue)
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum


if __name__ == "__main__":
    s = Solution()
    test_data = [-10, 9, 20, None, None, 15, 7]
    root = s.generate_tree(test_data)
    res = s.maxPathSum(root)
    print(res)
