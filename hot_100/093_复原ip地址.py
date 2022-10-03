# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/restore-ip-addresses/
题目难度：medium
解题思路: 得到所有组合->回溯，dfs
"""
from typing import List


class Solution:
    def dfs(self, s, depth, path, res):
        if depth == 4 and not s:   # 递归终止条件
            res.append(path[:-1])   # 去掉末尾的'.'
        for i in range(len(s)):
            if s[:i + 1] == '0' or (s[0] != '0' and 0 < int(s[:i + 1]) <= 255):  # 约束条件:前导不为0或者'0'单独为一段。
                self.dfs(s[i + 1:], depth + 1, path + s[:i + 1] + '.', res)

    def restoreIpAddress(self, s: str) -> List[str]:
        if not s or len(s) < 4 or len(s) > 12:
            return []
        res = list()
        self.dfs(s, 0, '', res)
        return res


if __name__ == "__main__":
    s = Solution()
    test = '101023'
    res = s.restoreIpAddress(test)
    print(res)
