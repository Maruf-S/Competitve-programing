class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = -1
        l = 1
        r = max(nums)
        def logic(div):
            num = 0
            for i in nums:
                num += (-(-i//div))
            return num
        while l <= r:
            m = (r + l)//2
            if logic(m) > threshold:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res