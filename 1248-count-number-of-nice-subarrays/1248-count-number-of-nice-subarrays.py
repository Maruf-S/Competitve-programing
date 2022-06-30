class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        oddCount = 0
        for r in range(len(nums)):
            if nums[r]%2 == 1:
                k-=1
                oddCount = 0
            while k == 0:
                if(nums[l] % 2 == 1):
                    k+=1
                oddCount +=1
                l+=1
            ans += oddCount
                
        return ans