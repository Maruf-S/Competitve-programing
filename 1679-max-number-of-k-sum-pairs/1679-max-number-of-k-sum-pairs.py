class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter()
        count = 0
        for i in nums:
            target = k - i
            if d[target] > 0:
                d[target] -= 1
                count += 1
            else:
                d[i] +=1
        return count
                