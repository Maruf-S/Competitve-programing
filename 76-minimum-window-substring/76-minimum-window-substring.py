class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcount = Counter(t)
        count = Counter()
        def doesWork():
            for k,v in tcount.items():
                if count[k] < v:
                    return False
            return True
        l = 0
        res = ["",float("inf")]
        for i,j in enumerate(s):
            count[j] += 1
            while doesWork():
                if i - l + 1 < res[1]:
                    res[0],res[1] = s[l : i + 1],i - l + 1
                count[s[l]] -= 1
                l += 1
        return res[0]