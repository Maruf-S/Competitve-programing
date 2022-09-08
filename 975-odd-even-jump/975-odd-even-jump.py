class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        def getNextIndex(sortedIdx):
            stack = []
            result = [None] * len(sortedIdx)
        
            for i in sortedIdx:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        
        sortedIdx = sorted(range(len(A)), key= lambda x: A[x])
        oddIndexes = getNextIndex(sortedIdx)
        sortedIdx.sort(key=lambda x: -A[x])
        evenIndexes = getNextIndex(sortedIdx)
        dp = [[0,1] for _ in range(len(A))]
        
        for i in range(len(A)):
            if oddIndexes[i] is not None:
                dp[oddIndexes[i]][0] += dp[i][1]
            if evenIndexes[i] is not None:
                dp[evenIndexes[i]][1] += dp[i][0]
				
        return dp[-1][0] + dp[-1][1]