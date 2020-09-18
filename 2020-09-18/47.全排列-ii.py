# @before-stub-for-debug-begin
from python3problem47 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start

import copy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        self.results = []
        self.dfs([False] * len(nums), [])
        return self.results
        
    def dfs(self, visited: List[int], current: List[int]):
        if len(current) == len(self.nums):
            self.results.append(copy.deepcopy(current))
            return
        for idx in range(len(visited)):
            if idx > 0 and self.nums[idx] == self.nums[idx - 1] and not visited[idx - 1]:
                continue
            if not visited[idx]:
                visited[idx] = True
                current.append(self.nums[idx])
                self.dfs(visited, current)
                current.pop()
                visited[idx] = False

# @lc code=end
