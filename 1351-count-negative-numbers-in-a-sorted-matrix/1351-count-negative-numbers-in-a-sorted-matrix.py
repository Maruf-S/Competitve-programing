class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def calcBin(row):
            l = 0
            r = len(row) - 1
            while l <= r:
                m = (l + r)//2
                if row[m] < 0:
                    r = m - 1
                else:
                    l = m + 1
            return len(row) - l
        count = 0
        for i in grid:
            count += calcBin(i)
        return count
            