"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        def get_idx(x, y):
            return x * m + y
        status = [[0 for _ in range(m)] for _ in range(n)]
        union_find_set = UnionFindSet(n * m)
        num_islands = 0
        results = []
        for point in operators:
            px, py = point.x, point.y
            if status[px][py] == 1:
                results.append(num_islands)
                continue
            num_islands += 1
            status[px][py] = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = px + dx, py + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or status[nx][ny] == 0:
                    continue
                if union_find_set.union(get_idx(px, py), get_idx(nx, ny)):
                    num_islands -= 1
            results.append(num_islands)
        return results
            

class UnionFindSet(object):
    def __init__(self, size):
        self.father = list(range(size))
    def find(self, x):
        if x == self.father[x]:
            return x
        else:
            fx = self.find(self.father[x])
            self.father[x] = fx
            return fx
    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fa] = fb
            return True
        return False
