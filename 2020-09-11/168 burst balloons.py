class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        if not nums:
            return 0
        # write your code here
        n = len(nums)
        nums = [1] + nums + [1]

        dp = [[0 for _ in range(n)] for _ in range(n)]  # dp[n][n]
        
        # initialization
        for idx in range(n):
            dp[idx][idx] = nums[idx] * nums[idx + 1] * nums[idx + 2]

        # dp algorithm, from small interval to large interval
        for interval in range(1, n):
            for s_idx in range(n - interval):
                e_idx = s_idx + interval
                max_score = 0
                for last_idx in range(s_idx, e_idx + 1):
                    max_score = max(max_score, get_score(s_idx, e_idx, last_idx, nums, dp))
                dp[s_idx][e_idx] = max_score
        return dp[0][n-1]
                
def get_score(s_idx, e_idx, last_idx, nums, dp):
    assert s_idx <= last_idx <= e_idx
    score = 0
    if last_idx > s_idx:
        score += dp[s_idx][last_idx - 1]
    if last_idx < e_idx:
        score += dp[last_idx + 1][e_idx]
    score += nums[last_idx + 1] * nums[s_idx] * nums[e_idx + 2]
    return score