class Solution(object):
    def merge(self,intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i<=len(intervals)-1:
            if(intervals[i][0]<=intervals[i-1][1]):
                merged = [intervals[i-1][0],max(intervals[i][1],intervals[i-1][1])]
                intervals.pop(i-1)
                intervals[i-1]=merged
            else:   
                i+=1
        return intervals