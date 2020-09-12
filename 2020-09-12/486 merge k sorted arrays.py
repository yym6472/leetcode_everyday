class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        from heapq import heappush, heappop
        heap = []
        results = []
        for array in arrays:
            if len(array) > 0:
                # (value, index, pointer of array)
                # the first item (value) as key to compare
                heappush(heap, (array[0], 0, array))
        while heap:
            item, idx, array_ptr = heappop(heap)
            results.append(item)
            idx = idx + 1
            if idx < len(array_ptr):
                heappush(heap, (array_ptr[idx], idx, array_ptr))
        return results