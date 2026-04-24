from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        path = [[0 for _ in range(n)] for _ in range(n)]

        start = (0,0)
        d = deque([start])
        path[0][0] = 1
        visited[0][0] = True

        dirs = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        while d:

            cur = d.popleft()
            x = cur[0]
            y = cur[1]

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    if grid[nx][ny] == 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        path[nx][ny] = path[x][y] + 1
                        d.append((nx,ny))

            if (x,y) == (n-1,n-1):
                break
        

        if path[n-1][n-1] == 0:
            return -1
        else:
            return path[n-1][n-1]


