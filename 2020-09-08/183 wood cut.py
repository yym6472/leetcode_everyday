class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # the binary search for "OOOXXXX" case
        #                          ↑
        def binary_search(start, end, check):
            left, right = start, end
            while left + 1 < right:
                mid = left + (right - left) // 2
                if check(mid):
                    left = mid
                else:
                    right = mid
            if check(right):  # case of "OOOOOOO"
                return right
            if check(left):  # case of "OOOXXXX"
                return left
            return 0  # when "XXXXXXX" happens, return 0 (indicates no answer)

        # defined the function for check "O" (True) or "X" (False) for a given index
        def check_cut(seg_len):
            seg_num = 0
            for length in L:
                seg_num += length // seg_len
            if seg_num >= k:
                return True
            else:
                return False
        
        # main function
        if not L:
            return 0
        max_length = max(L)
        return binary_search(1, max_length, check_cut)