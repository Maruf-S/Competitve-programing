class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return set(list(sentence)) == set(list("abcdefghijklmnopqrstuvwxyz"))