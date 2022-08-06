class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, totalTrips * min(time)
        while l <= r:
            m = (l + r)// 2
            trips = 0
            for i in time:
                trips += m//i
            if trips >= totalTrips:
                r = m - 1
            else:
                l = m + 1
        return l