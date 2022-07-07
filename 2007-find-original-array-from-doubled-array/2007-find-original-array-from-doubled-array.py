class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count  = Counter(changed)
        original = []
        changed.sort()
        for i in changed:
            if count[i] > 0:
                count[i]-=1
                if count[i*2] > 0:
                    original.append(i)
                    count[i*2]-=1
        if len(original) *2 == len(changed):
            return original
        return []