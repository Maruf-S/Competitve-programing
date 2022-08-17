class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t = 0
        rows,cols = len(grid),len(grid[0])
        fresh = 0
        q = deque([])
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j])
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for ir,jc in dirn:
                    row,col = r + ir, c + jc
                    if row == rows or col == cols or row < 0 or col < 0 or grid[row][col] != 1:
                        continue
                    fresh -= 1
                    grid[row][col] = 2
                    q.append((row,col))
            t += 1
        print(fresh)
        return t if fresh == 0 else -1