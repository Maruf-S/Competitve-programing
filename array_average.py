class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n=len(nums)
        ssum=sum(nums)
        if ssum==0:
            return True if n>1 else False
        @lru_cache(None)
        def subset_sum(idx,val,n1):
            if idx==n:
                return True if (val==0 and n1==0) else False
            res=False
            if val>=nums[idx]:
                res=res or subset_sum(idx+1,val-nums[idx],n1-1)
            res= res or subset_sum(idx+1,val,n1)
            return res
        for i in range(1,n):     #This is O(n)
            if (ssum*i)%n==0 and subset_sum(0,(ssum*i)//n,i):
                return True
        return False
