# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
#         def dfs(i,path,total,k):
#             if i > 9:
#                 return
#             if k == 0:
#                 print(path)
#                 if sum(path) == n:
#                     res.append(path[:])
#                 return
#             path.append(i)
#             dfs(i+ 1,path,total + i,k - 1)
#             path.pop()
#             dfs(i + 1,path,total,k)
#         res = []
#         dfs(1,[],0,k)
#         return res


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def backtrack(i,c,path,s):
            if len(path)==k:
                if s==n:
                    res.append(path[:])
                return
            if c>9:
                return
            path.append(c)
            backtrack(i+1,c+1,path,s+c)
            path.pop()
            backtrack(i,c+1,path,s)

        backtrack(0,1,[],0)
        return res