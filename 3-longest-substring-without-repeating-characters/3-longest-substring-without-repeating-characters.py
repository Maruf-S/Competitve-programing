class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res= 0
        used = {}
        
        for i,j in enumerate(s):
            if j in used and l<=used[j]:
                l = used[j] + 1
            else:
                res = max(res,i-l+1)
            used[j] = i
        return res