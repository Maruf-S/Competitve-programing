class Solution:
    def myPow(self,x, n):
        def powCalc(b, e):
            if(e == 0):
                return 1
            if(b == 0):
                return 0
            if(e % 2):
                res = powCalc(b,(e-1)/2)
                res = res*res*b # 5/2
                return res
            else:
                # Even exponent
                res = powCalc(b,e/2)
                res = res*res
                return res
        ans = powCalc(x,abs(n))
        return ans if n>0 else 1/ans