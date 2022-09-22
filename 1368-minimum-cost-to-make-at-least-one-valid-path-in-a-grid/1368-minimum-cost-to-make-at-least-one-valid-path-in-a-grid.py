class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        lecost = [[float("inf")]*len(grid[0]) for _ in range(len(grid))]
        rows,cols = len(grid),len(grid[0])
        dirn = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
        h = [(0,0,0)]
        while h:
            w,x,y = heappop(h)
            if w < lecost[x][y]:
                lecost[x][y] = w
                for d in dirn.values():
                    x1,y1 = x + d[0],y + d[1]
                    if x1 < 0 or x1 == rows or y1 < 0 or y1 == cols:
                        continue
                    if dirn[grid[x][y]] == d:
                        heappush(h,(w ,x + d[0], y + d[1]))
                    else:
                        heappush(h,(w + 1,x + d[0], y + d[1]))
        return lecost[-1][-1]