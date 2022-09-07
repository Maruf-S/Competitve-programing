class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        def withinBounds(rw,co):
            return rw < rows and rw >= 0 and co < cols and co >= 0
        visited = set()
        h = [(grid[0][0],0,0)]
        dirn = [(1,0),(0,1)]
        while h:
            w,r,c = heappop(h)          
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if r==rows-1 and c == cols - 1:
                return w
            for i1,j1 in dirn:
                nr,nc = r + i1, j1 + c
                if withinBounds(nr,nc) :
                    heappush(h,(w + grid[nr][nc],nr,nc))
            