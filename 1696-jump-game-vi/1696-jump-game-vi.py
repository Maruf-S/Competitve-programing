class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            ps = dq[0][0]+nums[i]
            # Keep it monotonic
            while dq and dq[-1][0] < ps:
                dq.pop()
            dq.append((ps, i))
            # Out of bounds
            if dq[0][1] == i-k:
                dq.popleft()
        return dq[-1][0]