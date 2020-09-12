class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp = [[0, 0, 0] for _ in range(n)]  # dp[n][3]
        dp[0][0] = distance(leaves[:1], 'r')
        dp[1][0] = distance(leaves[:2], 'rr')
        dp[1][1] = distance(leaves[:2], 'ry')
        dp[2][0] = distance(leaves[:3], 'rrr')
        dp[2][1] = min(distance(leaves[:3], 'rry'), distance(leaves[:3], 'ryy'))
        dp[2][2] = distance(leaves[:3], 'ryr')

        for idx in range(3, n):
            dp[idx][0] = dp[idx - 1][0] + (0 if leaves[idx] == 'r' else 1)
            dp[idx][1] = min(dp[idx - 1][0] + (0 if leaves[idx] == 'y' else 1),
                             dp[idx - 1][1] + (0 if leaves[idx] == 'y' else 1))
            dp[idx][2] = min(dp[idx - 1][1] + (0 if leaves[idx] == 'r' else 1),
                             dp[idx - 1][2] + (0 if leaves[idx] == 'r' else 1))
        return dp[n-1][2]

def distance(given, target):
    assert len(given) == len(target)
    result = 0
    for a, b in zip(given, target):
        if a != b:
            result += 1
    return result

solution = Solution()
print(solution.minimumOperations('ryr'))