class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s = []
        for i in intervals:
            if s and s[-1][1] >= i[0]:
                ele = s.pop()
                s.append([ele[0],max(ele[1],i[1])])
            else:
                s.append(i)
        return s
            