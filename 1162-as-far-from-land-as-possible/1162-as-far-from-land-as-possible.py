class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])    
        if len(q) == m * n or len(q) == 0: return -1
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        level = 0
        while q:
            for _ in range(len(q)):
                r,c= q.popleft()
                for i,j in dirn:
                    r1,c1 = r + i, c + j
                    if r1 == m or r1 < 0 or c1 == n or c1  < 0 or grid[r1][c1] == 1:
                        continue
                    q.append((r1,c1))
                    grid[r1][c1] = 1
            level += 1
        return level - 1
        # level = 0
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         i,j = q.popleft()
        #         for x,y in dirn:
        #             xi, yj = x+i, y+j
        #             if 0 <= xi < m and 0 <= yj < n and grid[xi][yj] == 0:
        #                 q.append((xi, yj))
        #                 grid[xi][yj] = 1
        #     level += 1
        # return level-1