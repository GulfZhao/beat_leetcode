# -*- coding: UTF-8 -*-
"""
题目链接: https://leetcode.cn/problems/partition-labels/
题目难度：medium
解题思路: 找到每个字符出现的位置最大的，用字典保存。遍历所有字符，如果
"""
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxindex = {}
        res = list()
        for i in range(len(s)):  # 记录每个字符最后的位置
            maxindex[s[i]] = i
        start, end = 0, 0
        for i in range(len(s)):   # 遍历整个字符串S，寻找所有合适的解
            end = max(maxindex[s[i]], end)
            if i == end:
                res.append(end-start+1)   # 计算片段长度
                start = end + 1           # 下个片段起始位置
        return res


# 测试用例
if __name__ == "__main__":
    s = Solution()
    test = "ababcbacadefegdehijhklij"
    res = s.partitionLabels(test)
    print(res)
