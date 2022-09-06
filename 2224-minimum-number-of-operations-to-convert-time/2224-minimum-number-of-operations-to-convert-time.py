class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = current.split(':')
        h2, m2 = correct.split(':')
        h = int(h2) - int(h1)
        m = int(m2) - int(m1)
        if m < 0:
            h -= 1
            m += 60
        
        a = m // 15
        m %= 15
        b = m // 5
        m %= 5
        return h + a + b + m