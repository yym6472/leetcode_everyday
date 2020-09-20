from typing import *

class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] -= i
        import heapq
        medians = []
        min_heap = []
        max_heap = []
        results = []
        for num in nums:
            if len(max_heap) == 0:
                heapq.heappush(max_heap, IntWrapper(num))
                results.append(0)
            elif len(min_heap) == len(max_heap) and num <= max_heap[0].value:
                heapq.heappush(max_heap, IntWrapper(num))
                results.append(medians[-1] - num)
            elif len(min_heap) == len(max_heap) and num > max_heap[0].value:
                heapq.heappush(min_heap, num)
                num_to_transfer = heapq.heappop(min_heap)
                heapq.heappush(max_heap, IntWrapper(num_to_transfer))
                results.append(num - max_heap[0].value)
            elif len(min_heap) + 1 == len(max_heap) and num <= max_heap[0].value:
                heapq.heappush(max_heap, IntWrapper(num))
                num_to_transfer = heapq.heappop(max_heap).value
                heapq.heappush(min_heap, num_to_transfer)
                results.append(medians[-1] - num)
            elif len(min_heap) + 1 == len(max_heap) and num > max_heap[0].value:
                heapq.heappush(min_heap, num)
                results.append(num - medians[-1])
            medians.append(max_heap[0].value)
        for i in range(1, len(results)):
            results[i] = (results[i - 1] + results[i]) % 1000000007
        return results

class IntWrapper(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    def __gt__(self, other):
        return self.value < other.value


solution = Solution()
print(solution.numsGame([1,1,1,2,3,4]))