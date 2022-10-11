class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = Counter(s)
        count2 = Counter(t)
        steps = 0
        andlay = set(list(s + t))
        for i in andlay:
            steps += abs(count2[i] - count1[i])
        return steps