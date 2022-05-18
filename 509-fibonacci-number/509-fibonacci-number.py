memo = {}
class Solution(object):
    def fib(self,N):
        if N == 0: return 0
        if N == 1: return 1
        if((N-1) not in memo):
            memo[N-1] = self.fib(N-1)
        if((N-2) not in memo):
            memo[N-2] = self.fib(N-2)
        return memo[N-1] + memo[N-2]
