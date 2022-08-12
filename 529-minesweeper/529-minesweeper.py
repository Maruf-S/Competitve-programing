class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        clr,clc = click[0],click[1]
        visited = set()
        if board[clr][clc] == "M":
            board[clr][clc] = "X"
            return board
        rows,cols = len(board),len(board[0])
#         def dfs(r,c):
#             if r == rows or r < 0 or c == cols or c < 0 or (r,c) in visited or board[r][c] != "E":
#                 return
#             # visited.add((r,c))
#             # if b == "M":
#             #     return
#             mines = 0
#             dirn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
#             for i,j in dirn:
#                 nr,nc = i + r, i + c
#                 if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M' :
#                     mines += 1
#             if mines > 0:
#                 board[r][c] = str(mines)
#                 return
#             else:
#                 board[r][c] = "B"
#             for i,j in dirn:
#                 nr,nc = i + r, i + c
#                 dfs(nr,nc)
        def dfs(r, c):
            if r == rows or r < 0 or c == cols or c < 0 or (r,c) in visited or board[r][c] != "E":
                return

            m, n = len(board), len(board[0])       
            directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

            mines = 0

            for d in directions:
                ni, nj = r + d[0], c + d[1]
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'M':        
                    mines += 1

            if mines > 0:
                board[r][c] = str(mines)
                return
            else:
                board[r][c] = "B"
            for i,j in directions:
                nr,nc = i + r, j + c
                dfs(nr, nc)
        dfs(clr,clc)
        return board