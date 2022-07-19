class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c = Counter(s1)
        s2c = {}
        s1l = len(s1)
        l = 0
        for i,j in enumerate(s2):
            s2c[j] = s2c.get(j,0) + 1
            while i - l + 1 > s1l:
                s2c[s2[l]] -= 1
                l += 1
            
            if i-l+1 >= s1l:
                res = True
                for k,v in s1c.items():
                    if k not in s2c or s2c[k] != v:
                        res = False
                        break
                if res:
                    return True
        return False