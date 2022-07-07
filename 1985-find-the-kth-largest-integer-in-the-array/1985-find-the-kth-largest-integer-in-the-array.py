class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        h = []
        for i in range(0,len(nums)):
            heapq.heappush(h,int(nums[i]))
            if len(h) > k:
                heapq.heappop(h)
        return str(h[0])