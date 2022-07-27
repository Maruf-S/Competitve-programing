class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        res = 0
        for k,v in count2.items():
            if v == 1 and count1[k] == 1:
                res += 1
        return res