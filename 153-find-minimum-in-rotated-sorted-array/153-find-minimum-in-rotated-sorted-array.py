class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findPivot(arr):
            last = arr[-1]
            l, r = 0, len(arr)-1
            while l<=r:
                m = (l+r)//2
                if arr[m] > last:
                    l = m + 1
                else:
                    r = m -1
            return l
        pivot = findPivot(nums)
        sechalf = nums[pivot:len(nums)]
        return sechalf[0]