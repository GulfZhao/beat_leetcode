# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
题目难度：medium
解题思路: 二叉树找
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent  # 适用于题目中节点有parent指针，原题不含parent指针


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':  # 时间复杂度为O(n),空间复杂度为O(n)
        if not root or root == p or root == q: return root  # 递归终止条件
        left = self.lowestCommonAncestor(root.left, p, q)  # 遍历左子树，找到最近公共祖先
        right = self.lowestCommonAncestor(root.right, p, q)  # 遍历右子树，找到最近公共祖先
        if not left and not right: return
        if not left: return right
        if not right: return left
        return root

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode',
                               q: 'TreeNode') -> 'TreeNode':  # 时间复杂度为O(n),空间复杂度为O(1), 树节点含有parent指针
        pass





