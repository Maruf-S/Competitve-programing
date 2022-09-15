class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        stoness = set(stones)
        visited = set()
        def dfs(val,units):
            if (val + units) not in stoness or (val, units) in visited:
                return False
            visited.add((val,units))
            if val + units == stones[-1]:
                return True
            return dfs(val + units,units) or dfs(val + units,units + 1) or dfs(val + units,units -1)
        # print(len(d))
        return dfs(0,1)