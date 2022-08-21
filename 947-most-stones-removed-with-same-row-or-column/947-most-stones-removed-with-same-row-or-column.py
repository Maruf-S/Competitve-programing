class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows,cols = defaultdict(list),defaultdict(list)
        s = set()
        for i,j in stones:
            rows[i].append(j)
            cols[j].append(i)
            s.add((i,j))
        def dfs(i,j):
            
            for c in rows[i]:
                if (i,c) not in s:
                    continue
                s.remove((i,c))
                dfs(i,c)
            for r in cols[j]:
                if (r,j) not in s:
                    continue
                s.remove((r,j))
                dfs(r,j)
        c  = 0
        for i,j in stones:
            if (i,j) in s:
                s.remove((i,j))
                dfs(i,j)
                c += 1
        return len(stones) - c