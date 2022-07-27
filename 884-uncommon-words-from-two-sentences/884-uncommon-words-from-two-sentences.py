class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        count1 = Counter(s1.split(" "))
        count2 = Counter(s2.split(" "))
        for k,v in count1.items():
            if v == 1 and count2[k] == 0:
                res.append(k)
        for k,v in count2.items():
            if v == 1 and count1[k] == 0:
                res.append(k)
        return res