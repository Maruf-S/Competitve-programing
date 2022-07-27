class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        counter = Counter((s1 + " " + s2).split(" "))
        return [k for k,v in counter.items() if v == 1]