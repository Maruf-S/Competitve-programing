class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x : x[1])
        end = float("-inf")
        erased = 0
        for i,j in intervals:
            if end <= i:
                end = j
            else:
                erased += 1
        return erased