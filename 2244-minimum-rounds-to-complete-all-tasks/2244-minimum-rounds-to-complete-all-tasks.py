class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        @cache
        def helper(i):
            if i == len(tasks):
                return 0
            res = float("inf")
            for j in range(i + 1,len(tasks)):
                if tasks[j] == tasks[i] and (j - i + 1 == 2 or j - i + 1 == 3):
                    res = min(res,1 + helper(j + 1))
                else:
                    break
            return res
        ans =  helper(0)
        return ans if ans!=float('inf') else -1