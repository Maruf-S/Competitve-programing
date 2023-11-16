class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s_nums = set(nums)
        choices = set()
        def permute(i,path):
            if i == n:
                choices.add(path)
                return
            permute(i + 1, path + "0")
            permute(i + 1, path + "1")
        permute(0,"")
        for choice in choices:
            if choice not in s_nums:
                return choice