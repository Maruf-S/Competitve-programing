class Solution:
    def minDistance(self, word1, word2):
        @lru_cache(None)
        def dp(i,j):
            if i < 0 or j < 0: return 0
            if word1[i] == word2[j]: 
                return dp(i-1,j-1) + 1
            else:
                return max(dp(i-1,j), dp(i,j-1))

        m, n = len(word1), len(word2)
        return m + n - 2*dp(m-1, n-1)