from typing import *

class Solution:
    def busRapidTransit(self, target: int, inc: int, dec: int, jump: List[int], cost: List[int]) -> int:
        self.cache = {}
        self.inc = inc
        self.dec = dec
        self.jump_cost = list(zip(jump, cost))
        return self.min_cost(target) % 1000000007

    def min_cost(self, target) -> int:
        if target == 0:
            return 0
        if target == 1:
            return self.inc
        if target in self.cache:
            return self.cache[target]
        
        result = 100000000000000
        for jump, cost in self.jump_cost:
            if target % jump == 0:
                tmp = self.min_cost(target // jump)
                result = min(result, tmp + cost)
                result = min(result, tmp + (target - target // jump) * self.inc)
            else:
                div_res = target // jump
                left_bound = div_res * jump
                right_bound = (div_res + 1) * jump
                tmp1 = self.min_cost(div_res)
                tmp2 = self.min_cost(div_res + 1)
                result = min(result, tmp1 + (target - left_bound) * self.inc + cost)
                result = min(result, tmp2 + (right_bound - target) * self.dec + cost)
                result = min(result, tmp1 + (target - div_res) * self.inc)
                result = min(result, tmp2 + (target - div_res - 1) * self.inc)

        self.cache[target] = result
        return result

solution = Solution()
print(solution.busRapidTransit(1000000000, 1, 1, jump = [2], cost = [200000]))