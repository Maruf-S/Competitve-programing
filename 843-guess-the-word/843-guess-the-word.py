class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        pattern = {}
        for word in words:
            for i,c in enumerate(word):
                pattern[(i,c)] = pattern.get((i,c),0) + 1
        def calculateProb(word):
            score = 0
            for i,c in enumerate(word):
                score += pattern.get((i,c),0) + 1
            return score
        words.sort(key = calculateProb)
        def canMatch(guess_word,word,matches):
            if guess_word == word:
                return False
            for x,y in zip(guess_word,word):
                if x == y:
                    matches -= 1
            return not matches
        idx = -1
        while words:
            words.sort(key = calculateProb)
            guess0 = words[idx]
            test = master.guess(guess0)
            if test == 6:
                break
            elif test == 0:
                words = [w for w in words if not any(a == b for a,b in zip(guess0,w))]
                idx = -1
            else:
                words = [w for w in words if canMatch(guess0,w,test)]
                idx = -1
                