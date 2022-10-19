class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        eleCount = [Counter(i) for i in strs]
        @cache
        def helper(i,total_0,total_1):
            if i == len(strs):
                if total_0 <= m and total_1 <= n:
                    return 0
            if total_0 > m or total_1 > n:
                return float("-inf")
            return max(1 + helper(i + 1,total_0 + eleCount[i]["0"],total_1 + eleCount[i]["1"]),helper(i + 1,total_0,total_1) )
        res=   helper(0,0,0)
        return 0 if res == float("-inf") else res