from typing import *

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        from bisect import bisect_right
        sorted_drinks = sorted(drinks)
        total = 0
        for each in staple:
            if x - each <= 0:
                continue
            total += bisect_right(sorted_drinks, x - each)
        return total % 1000000007

solution = Solution()
print(solution.breakfastNumber([1], [10, 20, 20, 20], 21))