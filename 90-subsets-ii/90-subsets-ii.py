class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(subset,i):
            if i == len(nums):
                return res.append(subset[::])
            
            subset.append(nums[i])
            dfs(subset,i + 1)
            subset.pop()
            if not subset or subset[-1] != nums[i]:                
                dfs(subset,i + 1)
        nums.sort()
        dfs([],0)
        return res


    
    
    
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(i, curSubset):
#             if i == len(nums):
#                 ans.append(curSubset[::])
#                 return

#             curSubset.append(nums[i])
#             backtrack(i + 1, curSubset)  # Pick
#             curSubset.pop()

#             if not curSubset or curSubset[-1] != nums[i]:
#                 backtrack(i + 1, curSubset)  # Don't pick

#         nums.sort()
#         ans = []
#         backtrack(0, [])
#         return ans