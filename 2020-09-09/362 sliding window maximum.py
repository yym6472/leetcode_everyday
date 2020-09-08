class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        if k > len(nums) or not nums:
            return []

        from collections import deque
        q = deque()
        for idx, num in enumerate(nums[:k]):
            if len(q) == 0:
                q.append((idx, num))
            else:
                pop_and_push(q, idx, num)
        results = [q[0][1]]
        for idx in range(len(nums) - k):
            r_idx = idx + k
            if q[0][0] == idx:
                q.popleft()
            pop_and_push(q, r_idx, nums[r_idx])
            results.append(q[0][1])
        return results

def pop_and_push(q, idx, num):
    while q and q[-1][1] <= num:
        q.pop()
    q.append((idx, num))