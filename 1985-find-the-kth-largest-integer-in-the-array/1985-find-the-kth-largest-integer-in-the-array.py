class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        h = []
        for i in range(k):
            heapq.heappush(h,nums[i])
        for i in range(k,len(nums)):
            if h[0] <= nums[i]:
                heapq.heappush(h,nums[i])
                if len(h) > k:
                    heapq.heappop(h)
        return str(heapq.heappop(h))