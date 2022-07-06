class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for i in matrix:
            for j in i:
                heapq.heappush(h,j)
        for i in range(k-1):
            heapq.heappop(h)
        return heapq.heappop(h)