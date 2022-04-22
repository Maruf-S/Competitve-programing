class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        output = []
        all_found = False
        for i in range(len(nums)):
            if(nums[i]==target):
                output.append(i)
            elif(all_found):
                break
        return output