class Solution(object):
    def findTheWinner(self, n, k):
        from collections import deque
        q = deque()
        for i in range(n,0,-1 ):
            q.append(i)
        while len(q) > 1:
            c = 1
            while c < k:
                q.appendleft(q.pop())
                c += 1
            q.pop()
        return q[0]