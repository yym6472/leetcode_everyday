class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        sorted_nums = sorted(list(set(nums)))
        num2idx = {number: idx for idx, number in enumerate(sorted_nums)}
        results = []
        nums.reverse()
        bit = BinaryIndexedTree(len(sorted_nums))
        for number in nums:
            results.append(bit.query(num2idx[number] - 1))
            bit.update(num2idx[number], 1)
        results.reverse()
        return results


class BinaryIndexedTree(object):
    def __init__(self, size: int) -> None:
        self.size = size
        self.data = [0] * size
    def update(self, pos: int, delta: int) -> None:
        assert 0 <= pos < self.size
        pos = pos + 1
        while pos <= self.size:
            self.data[pos - 1] += delta
            pos = pos + lowbit(pos)
    def query(self, pos: int) -> int:
        if pos < 0:
            return 0
        assert pos < self.size
        pos = pos + 1
        result = 0
        while pos > 0:
            result += self.data[pos - 1]
            pos = pos - lowbit(pos)
        return result


def lowbit(x: int) -> int:
    return x & -x


solution = Solution()
print(solution.countSmaller([5,2,6,1]))