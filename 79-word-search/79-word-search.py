class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        counter_word = Counter(word)
        
        
        counter_board = Counter()
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                counter_board[board[i][j]] += 1
                
        for ele in counter_word:
            if counter_word[ele] > counter_board[ele]:
                return False
        dirn = [[0,1],[0,-1],[1,0],[-1,0]]
        rows,cols = len(board),len(board[0])
        def dfs(i,j,k):
            if k == len(word):
                return True
            if 0 <= i < rows and 0 <= j < cols and (i,j) not in visited and board[i][j] == word[k]:
                k += 1
                visited.add((i,j))
                res = False
                for i1,j1 in dirn:
                    if dfs(i + i1,j + j1,k) == True:
                        res = True
                visited.remove((i,j))
                return res
            return False
        
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        return False