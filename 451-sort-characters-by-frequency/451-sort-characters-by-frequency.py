class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(list(s))
        res = ""
        for i,j in sorted(count.items(),key= lambda x: x[1],reverse=True):
            res+= i*j
        return res