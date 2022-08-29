class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path,index):
            res.append(path[::])
            for i in range(index,len(nums)):
                if i > index and nums[i -1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(path,i + 1)
                path.pop()
        nums.sort()
        dfs([],0)
        return res


    
# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         def backtrack(index, curSubset):
#             ans.append(curSubset[::])

#             for i in range(index, len(nums)):
#                 if i > index and nums[i] == nums[i - 1]: continue  # Skip duplicates
#                 curSubset.append(nums[i])
#                 backtrack(i + 1, curSubset)
#                 curSubset.pop()

#         nums.sort()
#         ans = []
#         backtrack(0, [])
#         return ans