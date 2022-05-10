class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = r = window = 0
        window = 0
        iq = collections.deque()
        dq = collections.deque()
        while(r < len(nums)):
            while dq and nums[dq[-1]]<=nums[r]:
                dq.pop()
            while iq and nums[iq[-1]]>=nums[r]:  
                iq.pop()
            iq.append(r)
            dq.append(r)
            # Keep shrinking th window from the 
            while nums[dq[0]] - nums[iq[0]] > limit:
                l+=1
                # Don need those ele no mo
                if iq[0] < l: iq.popleft()
                if dq[0] < l: dq.popleft()
            window = max(window,r-l+1)
            r+=1

        return window