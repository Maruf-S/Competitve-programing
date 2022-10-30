class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        @lru_cache(2000)
        def helper(i):
            if i == len(tasks):
                return 0
            res = float("inf")
            if i + 1 < len(tasks) and tasks[i] == tasks[i + 1]:
                res = min(res,1 + helper(i + 2))
            if i  + 2 < len(tasks) and tasks[i] == tasks[i + 2]:
                res = min(res, 1 + helper(i + 3))
            return res
        ans =  helper(0)
        return ans if ans!=float('inf') else -1