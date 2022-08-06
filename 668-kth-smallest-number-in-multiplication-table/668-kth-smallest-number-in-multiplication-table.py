class Solution:
    def findKthNumber(self, m, n, k):
        def getcount(mi,m,n):
            count = 0
            for i in range(1,m + 1):
                count += min(n,mi//i)
            return count
        l,r = 0 , m*n
        ans = -1
        while l <= r:
            mi = (l+r)//2
            if getcount(mi,m,n) >= k:
                r = mi - 1
            else:
                l = mi + 1
        return l