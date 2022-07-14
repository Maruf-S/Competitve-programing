class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0
        for i,j in enumerate(nums):
            while q and q[-1][1] < j:
                q.pop()
            q.append((i,j))
            
            while q[0][0] < l:
                q.popleft()
            if i + 1 >= k:
                res.append(q[0][1])
                l += 1
        return res