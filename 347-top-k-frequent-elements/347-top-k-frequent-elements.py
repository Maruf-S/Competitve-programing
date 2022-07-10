class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        from collections import Counter
        count  = Counter(nums)
        count = list(count.items())
        res = []
        # bc = [[]]* len(nums)
        bc = [[] for i in range(len(nums)+1)]
        for i,j in count:
            bc[j].append(i)
        res = []
        for i in bc[::-1]:
            res.extend(i)
            if len(res) >= k:
                return res
        