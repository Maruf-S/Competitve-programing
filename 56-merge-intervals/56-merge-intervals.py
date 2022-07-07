class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = []
        for i in intervals:
            if out and i[0] <= out[-1][1]:
                ele = out.pop()
                out.append([ele[0],max(ele[1],i[1])])
            else:
                out.append(i)
        return out