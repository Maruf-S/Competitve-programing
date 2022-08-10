class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac,atl = set(),set()
        rows = len(heights)
        cols = len(heights[0])
        def dfs(r,c,hs,prevh):
            if 0 <= r  < rows and 0 <= c  < cols and (r,c) not in hs and heights[r][c]  >= prevh :
                hs.add((r,c))
                dfs(r, c + 1,hs,heights[r][c])
                dfs(r, c - 1,hs,heights[r][c])
                dfs(r + 1, c ,hs,heights[r][c])
                dfs(r  - 1, c ,hs,heights[r][c])

        for i in range(cols):
            dfs(0,i,pac,float("-inf"))
            dfs(rows - 1,i,atl,float("-inf"))
        for i in range(rows):
            dfs(i,0,pac,float("-inf"))
            dfs(i,cols - 1,atl,float("-inf"))
        return pac.intersection(atl)
