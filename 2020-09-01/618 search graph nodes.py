"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        from collections import deque
        q = deque()
        q.append(node)
        visited = set([node])
        while q:
            curr = q.popleft()
            if values[curr] == target:
                return curr
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return None