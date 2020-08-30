class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count += 1
                    self.bfs((i, j), grid)
        return count
    
    def bfs(self, start, grid):
        from collections import deque
        q = deque()
        q.append(start)
        grid[start[0]][start[1]] = 0
        while q:
            x, y = q.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    q.append((nx, ny))