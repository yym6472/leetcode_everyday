class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        in_degree = [0] * numCourses
        neighbors = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            in_degree[i] += 1
            neighbors[j].append(i)
        from collections import deque
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        result = []
        while q:
            curr = q.popleft()
            result.append(curr)
            for neighbor in neighbors[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        if len(result) == numCourses:
            return result
        else:
            return []