class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter()
        for i in arr:
            if count[i * 2] > 0 or count[i / 2] > 0:
                return True
            count[i] += 1
        return False