class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        h = []
        for i in matrix:
            for j in i:
                heapq.heappush(h,-j)
                if len(h) > k:
                    heapq.heappop(h)
        return -heapq.heappop(h)