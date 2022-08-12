class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        s = len(M)
        seen = set()
        def dfs(i):
            seen.add(i)
            for j,val in enumerate(M[i]):
                if val and j not in seen:
                    dfs(j)
        cnt = 0
        for i in range(s):
            if i not in seen: 
                dfs(i)
                cnt += 1
        
        return cnt