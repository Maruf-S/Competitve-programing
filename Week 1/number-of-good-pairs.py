class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        dic = {}
        for i in nums:
            if i in dic:
                good_pairs += dic[i]
                dic[i]+=1
            else:
                dic[i] = 1
        return good_pairs