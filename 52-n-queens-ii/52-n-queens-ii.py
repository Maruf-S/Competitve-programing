class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDi = set()
        negDi = set()
        res = [0]
        board = [["."] * n for i in range(n)]
        def backtrack(r):
            if r == n:
                res[0] += 1
                return
                
            for c in range(n):
                if c not in col and r + c not in posDi and r - c not in negDi:
                    col.add(c)
                    posDi.add(r + c)
                    negDi.add(r - c)
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
                    col.remove(c)
                    posDi.remove(r + c)
                    negDi.remove(r - c)
        backtrack(0)
        return res[0]