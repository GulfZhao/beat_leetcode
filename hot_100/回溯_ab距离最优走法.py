# -*- coding: UTF-8 -*-
"""
题目链接: 非lc题目，题目内容，AB两地相距n米，i步走i米，每步可以向前或向后，求最优走法。
解题思路: 层次遍历，每层节点记录从起点走过的距离，当节点值等于n时结束循环，树的深度即代表所走的步数
"""


class Solution:

    def fromA2B(self, n: int) -> int:
        path = [0]
        depth = 0
        while path:
            depth += 1
            size = len(path)
            while size > 0:
                cur_sum = path.pop(0)
                for i in [-1, 1]:
                    new_sum = cur_sum + depth * i
                    if new_sum == n:
                        return depth
                    path.append(new_sum)
                size -= 1
        return 0


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test = 11
    res = s.fromA2B(test)
    print("result: %d " % res)
