class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        first, last = A[0], A[-1]
        res = last - first
        for i in range(len(A) - 1):
            maxi = max(A[i] + K, last - K)
            mini = min(first + K, A[i + 1] - K)
            res = min(res, maxi - mini)
        return res