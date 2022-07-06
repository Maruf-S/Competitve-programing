class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        from collections import Counter
        from operator import itemgetter
        count  = Counter(nums)
        count = list(count.items())
        count.sort(key=lambda x:x[1],reverse=True)
        i = 0
        while i<k:
            result.append(count[i][0])
            i+=1
        return result