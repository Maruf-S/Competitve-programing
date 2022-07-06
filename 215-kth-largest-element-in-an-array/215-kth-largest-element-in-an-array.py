class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # for i in range(len(nums)-k):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)
        h = []
        for i in nums:
            heapq.heappush(h,-i)
        for i in range(k-1):
            heapq.heappop(h)
        return -heapq.heappop(h)