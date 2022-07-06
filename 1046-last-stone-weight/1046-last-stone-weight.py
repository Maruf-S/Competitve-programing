class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-i for i in stones]
        heapq.heapify(h)
        while len(h) > 1:
            x = heapq.heappop(h) * -1
            y = heapq.heappop(h) * -1
            if x == y:
                continue
            heapq.heappush(h,-(x-y))
        if h:
            return -(heapq.heappop(h))
        return 0