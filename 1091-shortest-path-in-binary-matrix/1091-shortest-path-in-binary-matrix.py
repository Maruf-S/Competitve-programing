class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirn = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        if grid[0][0] == 1:
            return -1
        q = deque([(0,0)])
        visited = set([(0,0)])
        rows,cols = len(grid),len(grid[0])
        res = 1
        while q:
            for i in range(len(q)):
                cell = q.popleft()
                if cell == (rows - 1,cols - 1):
                    return res
                for i1,j1 in dirn:
                    nr,nc = i1+ cell[0], j1 + cell[1]
                    if 0<= nr <rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 0:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            res += 1
        return -1