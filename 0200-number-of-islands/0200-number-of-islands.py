from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        cnt = 0 

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "1" and not visited[i][j]:
                    d = deque([(i,j)])
                    visited[i][j] = True
                    cnt += 1
        
                    while d:

                        cur = d.popleft()
                        x = cur[0]
                        y = cur[1]            

                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]

                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == "1" and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    d.append((nx,ny))

        return cnt