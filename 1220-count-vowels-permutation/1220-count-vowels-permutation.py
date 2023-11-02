class Solution:
    def countVowelPermutation(self,rn: int) -> int:
        
        @cache
        def dp(n,char):
            if n == 0:
                return 1
            if char == "a":
                return dp(n - 1,"e") % (10 ** 9 + 7)
            if char == "e":
                return (dp(n - 1,"a") + dp(n - 1,"i"))% (10 ** 9 + 7)
            if char == "i":
                return sum(dp(n - 1, i) for i in "aeou")% (10 ** 9 + 7)
            if char == "o":
                return sum(dp(n - 1, i) for i in "iu")% (10 ** 9 + 7)
            if char == "u":
                return dp(n - 1, "a")% (10 ** 9 + 7)
        return sum(dp(rn - 1,k) for k in "aeiou")% (10 ** 9 + 7)