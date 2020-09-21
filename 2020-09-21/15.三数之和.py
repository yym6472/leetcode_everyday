#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j, k in self.two_sum(nums, i + 1, len(nums) - 1, -nums[i]):
                results.add((nums[i], nums[j], nums[k]))
        return list(results)

    def two_sum(self, nums, start, end, target):
        left, right = start, end
        while left < right:
            if nums[left] + nums[right] == target:
                yield left, right
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                right -= 1

# @lc code=end

