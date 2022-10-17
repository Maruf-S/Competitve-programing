class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        @cache
        def helper(total,cur,flag):
            # print(total,cur,flag)
            if total == n:
                return 0
            if total > n or cur > n:
                return float("inf")
            if flag:
                return 1 + helper(total + cur,cur,False)
            else:
                return 1 + min(helper(total + cur,cur,False),helper(total,total,True))
        return helper(0,1,True)