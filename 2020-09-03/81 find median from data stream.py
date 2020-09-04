class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        import heapq
        medians = []
        min_heap = []
        max_heap = []
        for num in nums:
            if len(max_heap) == 0:
                heapq.heappush(max_heap, IntWrapper(num))
            elif len(min_heap) == len(max_heap) and num <= max_heap[0].value:
                heapq.heappush(max_heap, IntWrapper(num))
            elif len(min_heap) == len(max_heap) and num > max_heap[0].value:
                heapq.heappush(min_heap, num)
                num_to_transfer = heapq.heappop(min_heap)
                heapq.heappush(max_heap, IntWrapper(num_to_transfer))
            elif len(min_heap) + 1 == len(max_heap) and num <= max_heap[0].value:
                heapq.heappush(max_heap, IntWrapper(num))
                num_to_transfer = heapq.heappop(max_heap).value
                heapq.heappush(min_heap, num_to_transfer)
            elif len(min_heap) + 1 == len(max_heap) and num > max_heap[0].value:
                heapq.heappush(min_heap, num)
            medians.append(max_heap[0].value)
        return medians


class IntWrapper(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    def __gt__(self, other):
        return self.value < other.value


solution = Solution()
print(solution.medianII([4,5,1,3,2,6,0]))