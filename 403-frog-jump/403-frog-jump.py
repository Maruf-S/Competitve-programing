class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        def dfs(i,unit,total):
            if (i,unit,total) in d:
                return d[(i,unit,total)]
            if i == len(stones) - 1:
                if stones[i] == total:
                    return True
                else:
                    return False
            # elif i >= len(stones):
            #     return False
            if total == stones[i]:
                d[(i,unit,total)] = dfs(i + 1, unit - 1, total + (unit - 1)) or dfs(i + 1,unit,total + unit) or dfs(i + 1,unit + 1,total + (unit + 1))
            elif total > stones[i]:
                d[(i,unit,total)] = dfs(i + 1,unit,total)
            else:
                d[(i,unit,total)] =  False
            return d[(i,unit,total)]
        x = dfs(1,1,1)
        # print(d)
        return x