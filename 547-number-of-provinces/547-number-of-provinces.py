class Solution:
    def findCircleNum(self, c: List[List[int]]) -> int:
        visited = set()
        def dfs(city):
            visited.add(city)
            for i in range(len(c)):
                if i not in visited and c[city][i] == 1:
                    dfs(i)
        res = 0
        for city in range(len(c)):
            if city not in visited:
                dfs(city)
                res += 1
        return res