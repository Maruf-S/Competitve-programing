class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @functools.lru_cache(None)
        def gc(i):
            if i >= len(days):
                return 0
            miim = float("inf")
            for p,c in zip([1,7,30],costs):
                j = i
                while j < len(days) and days[j] < days[i] + p:
                    j += 1
                miim = min(miim,c + gc(j))
            return miim
        return gc(0)