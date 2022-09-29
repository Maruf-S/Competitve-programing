class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            while q and i - q[0] + 1 > k :
                q.popleft()
            if i > k - 2:
                res.append(nums[q[0]])
            
        return res