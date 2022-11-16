class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        bound = lambda row, col: 0 <= row < rows and 0 <= col < cols
        adj, ans = [0, 1], []
        count, times = 0, 1
        size = max(rows, cols)**2
        
        while count < 4*size:
            for i in range(2):
                for j in range(times):
                    if bound(rStart, cStart):
                        ans.append([rStart, cStart])
                    
                    rStart += adj[0]
                    cStart += adj[1]
                    count += 1
                    
                adj[0], adj[1] = adj[1], -1*adj[0]
                
            times += 1
            
        return ans
