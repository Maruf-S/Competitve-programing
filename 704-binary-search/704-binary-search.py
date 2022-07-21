class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def recur(l,r):
            mid = (l + r) //2
            if l > r:
                return -1
            if nums[mid] < target:
                return recur(mid+1,r)
            elif nums[mid] > target:
                return recur(l,mid -1)
            else:
                return mid
        return recur(0,len(nums) - 1)