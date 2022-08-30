# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
#         def dfs(i,path,total,k):
#             if i > 9:
#                 return
#             if k == 0:
#                 if sum(path) == n:
#                     res.append(path[::])
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
        def backtrack(i,c,r,s):
            if i==k:
                if s==n:
                    res.append(r[:])
                    return
                else:
                    return
            if i>=k or c>9:
                return
            r.append(c)
            backtrack(i+1,c+1,r,s+c)
            r.pop()
            backtrack(i,c+1,r,s)

        backtrack(0,1,[],0)
        return res