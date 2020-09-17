from typing import *
from collections import deque

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        neighbors = {}
        neighbors_rev = {}
        for i in range(1, n+1):
            neighbors[i] = []
            neighbors_rev[i] = []
        for u, v in edges:
            neighbors[u].append(v)
            neighbors_rev[v].append(u)
        
        # topological sort
        in_degrees = {i: len(neighbors[i]) + len(neighbors_rev[i]) for i in range(1, n+1)}
        visited = set()
        q = deque()
        for i in range(1, n+1):
            if in_degrees[i] == 1:
                q.append(i)
                visited.add(i)
        while q:
            cur = q.popleft()
            for neighbor in neighbors[cur] + neighbors_rev[cur]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        circle_node = []
        degree_two_node = None
        for i in range(1, n+1):
            if i not in visited:
                circle_node.append(i)
                if len(neighbors_rev[i]) == 2:
                    assert degree_two_node is None
                    degree_two_node = i
                    
        candidates = []
        if degree_two_node is None:  # 形成了一个环，那么环上的每条边都可以去除
            for node in circle_node:
                candidates.append((neighbors_rev[node][0], node))
        else:  # 没有形成环，需要去除入度为二的节点的其中一条边
            for neighbor_rev_node in neighbors_rev[degree_two_node]:
                if neighbor_rev_node in circle_node:  # 仅当这条边在环路上，才将其考虑进去
                    candidates.append((neighbor_rev_node, degree_two_node))
        
        edge2idx = {(item[0], item[1]): idx for idx, item in enumerate(edges)}
        return max(candidates, key=lambda x: edge2idx[x])

solution = Solution()
print(solution.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]]))