class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash = {0:-1}
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            # _sum %=k
            if (_sum % k ) in hash:
                if i - hash[(_sum % k)]  >= 2:
                    return True
            else:
                hash[_sum % k] = i
        return False            
            