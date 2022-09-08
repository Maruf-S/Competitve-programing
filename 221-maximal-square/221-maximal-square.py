class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        d = {}
        def helper(r,c):
            if r == rows or c == cols:
                return 0
            if (r,c) in d:
                return d[(r,c)]
            top,bot,diag = helper(r + 1,c),helper(r,c + 1),helper(r+1,c+1)
            d[(r,c)] = 0
            if matrix[r][c] == "1":
                d[(r,c)] = 1 + min(top,bot,diag)
            return d[(r,c)]
        helper(0,0)
        return max(d.values())**2