class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        count  = Counter(arr)
        count = list(count.values())
        count.sort()
        sum_val = 0
        array_half = (len(arr)+1)//2
        res = 0
        for i in range(len(count)-1,-1,-1):
            sum_val+=count[i]
            res+=1
            if(sum_val>=array_half):
                return res