# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/binary-tree-preorder-traversal/
解题思路: 前序遍历：根节点-左-右,中序遍历：左-根节点-右，后序遍历：左-右-根节点
解法1：递归，前序、中序、后序的递归解法几乎一致，区别仅在于append value的的顺序
解法2：非递归算法，也是重点考察的点。前序遍历：
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

    def preorderTraversal(self, root: TreeNode) -> List[int]:  # 前序遍历递归解法
        def preorder(root):
            if not root: return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        res = []
        preorder(root)
        return res

    def preorderTraversal_2(self, root: TreeNode) -> List[int]:  # 前序遍历非递归算法，借助栈先入后出
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:  # 中序遍历递归解法
        def inorder(root):
            if not root: return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        res = []
        inorder(root)
        return res

    def inorderTraversal_2(self, root: TreeNode) -> List[int]:  # 中序遍历非递归解法，借助栈
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)    # 将cur入栈，并到达最左端的叶子节点
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)  # 出栈时，加入到结果中
            cur = cur.right
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:  # 后序遍历递归解法
        def postorder(root):
            if not root: return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        res = []
        postorder(root)
        return res

    def postorderTraversal_2(self, root: TreeNode) -> List[int]:  # 后序遍历非递归解法(借助2个栈)
        stack = [root]       # 进栈顺序：左，右，根，出栈顺序，根，右，左
        stack_2 = []         # 接收stack弹出结果
        res = []
        while stack:
            node = stack.pop()
            stack_2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack_2:
            node = stack_2.pop()
            res.append(node.val)
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    root = s.test_case()
    res = s.inorderTraversal_2(root)
    print(res)
