class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9+7
        h = 2**p - 2                                   
        n = 2**(p-1)-1
    
        return ((pow(h,n,MOD))*(h+1))%MOD