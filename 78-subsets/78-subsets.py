# class Solution(object):
#     def subsets(self, nums):
#         ret = []
#         self.dfs(nums, [], ret)
#         return ret
    
#     def dfs(self, nums, path, ret):
#         ret.append(path)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:], path+[nums[i]], ret)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        # subset = []
        def dfs(i,subset):
            if i >= len(nums):
                return res.append(subset[:])
            subset.append(nums[i])
            dfs(i + 1,subset)
            
            subset.pop()
            dfs(i + 1,subset)
        dfs(0,[])
        return res