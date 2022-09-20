class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left,end = Counter(nums),defaultdict(int)
        for num in nums:
            if not left[num]:
                continue
            if end[num - 1]:
                left[num] -= 1
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] > 0 and left[num + 2] > 0:
                left[num + 1] -= 1
                left[num + 2] -= 1
                left[num] -= 1
                end[num + 2] += 1
            else:
                return False
        return True