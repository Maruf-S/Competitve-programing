class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @cache
        def magic(i,s1,s2):
            if i == len(stones):
                return abs(s1 - s2)
            return min(magic(i + 1,s1 + stones[i],s2),magic(i + 1,s1,s2 + stones[i]))
        
        return magic(0,0,0)