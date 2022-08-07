class Solution:
    def minDays(self, bloomDay: List[int], mr: int, k: int) -> int:
        def sufficent(d):
            bouquet = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= d:
                    flowers += 1
                else:
                    flowers = 0
                    # Streak
                if flowers == k:
                    bouquet += 1
                    flowers = 0
            return bouquet >= mr
        l,r = 1,max(bloomDay)
        res = -1
        while l <= r:
            m = (l + r)//2
            if sufficent(m):
                res = m
                r = m - 1
            else:
                l = m + 1
                
        return res