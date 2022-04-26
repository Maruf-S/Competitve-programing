def maxFrequency(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    l = r = total = window = 0
    while r < len(nums):
        total += nums[r]
        while(nums[r]*(r-l+1)>total+k):
            total -= nums[l]
            l+=1
        window = max(r-l+1,window)
        r += 1
    return window


maxFrequency([1, 4, 8, 13])
