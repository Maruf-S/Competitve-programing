class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(i,j):
            if i >= len(triangle) or j >= len(triangle[i]):
                return 0
            return triangle[i][j] + min(dfs(i + 1,j),dfs(i + 1,j +  1))
        return dfs(0,0)