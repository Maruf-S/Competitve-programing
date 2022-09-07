class Solution:
    def isToeplitzMatrix(self, arr: List[List[int]]) -> bool:
          visited = set()
          rows,cols = len(arr),len(arr[0])
          def dfs(r,c,val):
            if r == rows or c == cols or (r,c) in visited:
              return True
            if arr[r][c] != val:
              return False
            visited.add((r,c))
            return dfs(r + 1, c + 1,val)
          for i in range(rows):
            for j in range(cols):
              if not dfs(i,j,arr[i][j]):
                return False
          return True