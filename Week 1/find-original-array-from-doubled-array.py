from collections import Counter
class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        changed.sort()
        count  = Counter(changed)
        original = []
        for i in changed:
            if(count[i]>0):
                count[i] -=1
                if(count[i*2] >0):
                    original.append(i)
                    count[i*2]  -=1
        if len(original)*2 == len(changed):
            return original
        return []