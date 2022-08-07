class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def logic(speed):
            hr = 0
            for i in range(0,len(dist) - 1):
                hr += (-(-dist[i]//speed))
            hr += dist[-1]/speed
            print(hr)
            return hr
        l = 1
        r = 10000000
        res =  -1
        while l <= r:
            m = (l + r)//2
            hr = logic(m)
            if hr <= hour:
                res = m
                r = m - 1
            elif hr > hour:
                l = m + 1
        return res