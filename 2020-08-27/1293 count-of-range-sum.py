class Solution:
    """
    @param nums: a list of integers
    @param lower: a integer
    @param upper: a integer
    @return: return a integer
    """
    def countRangeSum(self, nums, lower, upper):
        from bisect import bisect_left
        sums = [0] * (len(nums) + 1)
        sums[0] = 0
        for i in range(len(nums)):
            sums[i+1] = sums[i] + nums[i]
        sorted_sums = sorted(list(set(sums)))
        bit = BinaryIndexedTree(len(sorted_sums))
        counter = 0
        for i in range(len(sums)):
            left_bound = sums[i] - upper  # currect_sum - left_bound = upper
            right_bound = sums[i] - lower # currect_sum - right_bound = lower
            # 统计之前出现的，sum在[left_bound, right_bound + 1)之间的个数
            lower_count = bit.query(bisect_left(sorted_sums, left_bound) - 1)
            upper_count = bit.query(bisect_left(sorted_sums, right_bound + 1) - 1)
            counter += (upper_count - lower_count)
            bit.update(bisect_left(sorted_sums, sums[i]), 1)
        return counter


class BinaryIndexedTree(object):
    def __init__(self, size: int) -> None:
        self.size = size
        self.data = [0] * size
    def update(self, pos: int, delta: int) -> None:
        assert pos >= 0 and pos < self.size
        pos += 1
        while pos <= self.size:
            self.data[pos - 1] += delta
            pos += lowbit(pos)
    def query(self, pos: int) -> int:
        if pos < 0:
            return 0
        assert pos >= 0 and pos < self.size
        pos += 1
        result = 0
        while pos > 0:
            result += self.data[pos - 1]
            pos -= lowbit(pos)
        return result


def lowbit(x: int) -> int:
    return x & -x