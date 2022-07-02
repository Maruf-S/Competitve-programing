class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        for i,j in enumerate(word):
            if j in "aeiou":
                count += (len(word)-i)*(i+1)
        return count