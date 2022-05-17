class Solution(object):
    def findTheWinner(self, n, k):
        q = []
        for i in range(n,0,-1 ):
            q.append(i)
        while len(q) > 1:
            c = 1
            while c < k:
                q.insert(0,q.pop())
                c += 1
            q.pop()
        return q[0]