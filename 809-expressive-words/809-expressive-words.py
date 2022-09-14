class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def let_count(w):
            cnt = []
            for ch in w:
                if not cnt or cnt[-1][0] != ch:
                    cnt.append([ch, 0])
                cnt[-1][1] += 1
            return cnt
        
        let_s = let_count(s)
        def check(word):
            let_w = let_count(word)
            if len(let_s) != len(let_w): return False
            for i in range(len(let_s)):
                ch1, cnt1 = let_s[i]
                ch2, cnt2 = let_w[i]
                if ch1 != ch2: return False
                if cnt1 < cnt2 or (cnt1 < 3 and cnt1 != cnt2):
                    return False
            return True
        return sum([check(w) for w in words])