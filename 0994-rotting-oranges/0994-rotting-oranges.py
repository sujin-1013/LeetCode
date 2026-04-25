from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        d = deque([])
        time = 0
        fresh = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    d.append((i,j))
                    
                elif grid[i][j] == 1:
                    fresh += 1
                

        while d and fresh > 0:
            time += 1

            for _ in range(len(d)):

                cur = d.popleft()

                x = cur[0]
                y = cur[1]

                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            d.append((nx, ny))

        if fresh > 0:
            return -1
        
        return time