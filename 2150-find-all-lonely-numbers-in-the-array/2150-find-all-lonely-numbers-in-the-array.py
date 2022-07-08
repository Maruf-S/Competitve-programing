class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = []
        for i in nums:
            if count[i] == 1 and count[i+1] == 0 and count[i-1] == 0:
                ans.append(i)
        return ans