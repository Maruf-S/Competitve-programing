class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        d = {}
        res = [0]
        def dfs(i,k):
            if (i,k) in d:
                return d[(i,k)]
            if k == 0:
                if i == endPos:
                    return 1
                return 0
            res = dfs(i - 1,k - 1) + dfs(i + 1, k - 1)
            d[(i,k)] = res
            return d[(i,k)]
        return dfs(startPos,k)%(10**9+7)