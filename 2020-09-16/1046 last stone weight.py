class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush, heappop
        heap = []
        for stone in stones:
            heappush(heap, StoneWrapper(stone))
        while len(heap) > 1:
            first = heappop(heap).value
            second = heappop(heap).value
            if first != second:
                heappush(heap, StoneWrapper(abs(first - second)))
        if heap:
            return heappop(heap).value
        else:
            return 0
                

class StoneWrapper(object):
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value
    def __gt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value