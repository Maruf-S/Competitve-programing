class Solution(object):
    def generateMatrix(self,n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        l = 0
        r = n
        t = 0
        b = n
        ni = 1
        res = [[0]*n for _ in range(n)]
        while l < r and t < b:
            for i in range(l, r):
                res[t][i] = ni
                ni+=1
            t+=1
            for i in range(t,b):
                res[i][r-1] = ni
                ni+=1
            r-=1
            # if not (l<r and t<b):
            #     break
            for i in range(r-1,l-1,-1):
                res[b-1][i] = ni
                ni+=1
            b-=1
            for i in range(b-1,t-1,-1):
                res[i][l] = ni
                ni+=1
            l+=1   
            # break     
        return res
