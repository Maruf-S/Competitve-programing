class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        rows,cols = len(matrix),len(matrix[0])
        dirn = [[1,0],[-1,0],[0,1],[0,-1]]
        cache = {}
        def dfs(r,c,cmp):
            if r == rows or r < 0 or c < 0 or c == cols or matrix[r][c] <= cmp:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            
            ans =  1 + max([dfs(r + r1, c + c1,matrix[r][c]) for r1,c1 in dirn])
            cache[(r,c)] = ans
            return ans
        for i in range(rows):
            for j in range(cols):
                res = max(res,dfs(i,j,float("-inf")))
        return res