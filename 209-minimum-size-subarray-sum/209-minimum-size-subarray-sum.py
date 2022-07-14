class Solution:
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        n = len(nums) + 1
        mw = n
        cur = 0
        q = deque()
        for i,j in enumerate(nums):
            cur += j
            if cur >= k:
                mw = min(mw,i+1)
            while q and cur - q[0][1] >= k:
                mw = min(mw,i-q.popleft()[0])
            q.append([i,cur])
        return mw if mw!=n else 0