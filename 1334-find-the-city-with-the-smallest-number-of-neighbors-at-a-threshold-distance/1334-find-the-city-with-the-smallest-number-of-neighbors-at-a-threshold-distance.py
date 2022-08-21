class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], kk: int) -> int:
        distance = [[float("inf")]*n for i in range(n)]
        
        for i in range(n):
            distance[i][i] = 0
            
        for n1, n2, w in edges:
            distance[n1][n2] = w
            distance[n2][n1] = w
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist = distance[i][k] + distance[k][j]
                    if dist < distance[i][j]:
                        distance[i][j] = dist
                        distance[j][i] = dist
        nei = [0] * n
        for i in range(n):
            for j in range(n):
                nei[i] += 1 if distance[i][j] <= kk else 0
        res,mini = None, float("inf")
        for i in range(n):
            if nei[i] <= mini:
                mini = nei[i]
                res = i
        return res