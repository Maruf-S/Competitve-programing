class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        def dfs(i,j,n):
            if i >= rows or i < 0 or j < 0 or j >= cols or (i,j) in visited or board[i][j] != word[n]:
                return False
            if board[i][j] == word[n] and n == len(word)-1:
                return True
            visited.add((i,j))
            res = False
            if board[i][j] == word[n]:
                dirn = [[1,0],[-1,0],[0,1],[0,-1]]
                for r,c in dirn:
                    if dfs(i + r,j + c,n + 1) == True:
                        res = True
            visited.remove((i,j))
            return res
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row,col,0) == True:
                    return True