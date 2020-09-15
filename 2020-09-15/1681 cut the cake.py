class Solution:
    """
    @param n: the length of the cake
    @param m: the width of the cake
    @param k: the number of the strewberries
    @param mp: the position of the k strewberries
    @return: the shortest cut length
    """
    def getTheShortestCutLength(self, n, m, k, mp):
        self.n = n
        self.m = m
        self.mp = mp
        self.buffer = {}
        if n == 0 or m == 0 or k == 0:
            return 0
        return self.dfs(0, m - 1, n - 1, 0)

    def dfs(self, left, right, upper, lower):
        if (left, right, upper, lower) in self.buffer:
            return self.buffer[(left, right, upper, lower)]
        if left > right or upper < lower:
            return None
        s_count = self.count_strewberries(left, right, upper, lower, self.mp)
        if s_count == 0:
            self.buffer[(left, right, upper, lower)] = None
            return None
        if s_count == 1:
            self.buffer[(left, right, upper, lower)] = 0
            return 0
        
        min_cuts = 100000000
        for cut in range(right - left):
            left_cuts = self.dfs(left, left+cut, upper, lower)
            right_cuts = self.dfs(left+cut+1, right, upper, lower)
            if left_cuts is not None and right_cuts is not None:
                min_cuts = min(min_cuts, left_cuts + right_cuts + upper - lower + 1)
        for cut in range(upper - lower):
            lower_cuts = self.dfs(left, right, lower+cut, lower)
            upper_cuts = self.dfs(left, right, upper, lower+cut+1)
            if lower_cuts is not None and upper_cuts is not None:
                min_cuts = min(min_cuts, lower_cuts + upper_cuts + right - left + 1)
        self.buffer[(left, right, upper, lower)] = min_cuts
        return min_cuts
        

    def count_strewberries(self, left, right, upper, lower, mp):
        count = 0
        for strewberry in mp:
            if self.check(strewberry, left, right, upper, lower):
                count += 1
        return count

    def check(self, pos, left, right, upper, lower):
        x, y = pos
        x, y = x - 1, y - 1
        return left <= y <= right and lower <= x <= upper

solution = Solution()
print(solution.getTheShortestCutLength(3, 4, 3, [[1, 2], [2, 3], [3, 2]]))