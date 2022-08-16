class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [(grid[0][0],0,0)]
        visit = set()
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        while h:
            th,r,c = heappop(h)
            if r >=n or c >=n or r < 0 or c < 0 or (r,c) in visit:
                continue
            visit.add((r,c))
            if r == n - 1 and c == n - 1:
                return th
            for ir,ic in dirn:
                nr,nc = ir + r, c + ic
                if nr >=n or nc >=n or nr < 0 or nc < 0 or (nr,nc) in visit:
                    continue
                heappush(h,(max(th,grid[nr][nc]),nr,nc))
        
# [[3,2]
#  [0,1]]