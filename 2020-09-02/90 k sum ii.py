import copy

class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        self.A = A
        self.k = k
        all_solutions = []
        self.dfs(all_solutions, [], target, 0)
        return all_solutions
    
    def dfs(self, all_solutions, current_list, target, idx):
        if target == 0 and len(current_list) == self.k:
            all_solutions.append(copy.deepcopy(current_list))
            return
        if target < 0:
            return
        if len(current_list) > self.k:
            return
        if idx >= len(self.A):
            return
        self.dfs(all_solutions, current_list, target, idx + 1)
        current_list.append(self.A[idx])
        self.dfs(all_solutions, current_list, target - self.A[idx], idx + 1)
        current_list.pop(-1)