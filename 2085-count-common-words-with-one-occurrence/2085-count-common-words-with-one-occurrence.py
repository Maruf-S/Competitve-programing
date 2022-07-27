class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)
        res = 0
        if len(count1) > len(count2):
            for k,v in count2.items():
                if v == 1 and count1[k] == 1:
                    res += 1
        else:
            for k,v in count1.items():
                if v == 1 and count2[k] == 1:
                    res += 1
        return res