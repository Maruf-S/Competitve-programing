class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1] * n
        pairs.sort()
        for i in range(n-2,-1,-1):
            temp = 1
            for j in range(i+1,n):
                n1,n2 = pairs[i],pairs[j]
                if n1[1] < n2[0]:
                    temp = max(temp,dp[j] + dp[i])
            dp[i] = temp
        return max(dp)
                