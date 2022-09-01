class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        col = collections.defaultdict(int)
        row = collections.defaultdict(int)
        diag1 = collections.defaultdict(int)
        diag2 = collections.defaultdict(int)
        lamps = set((i, j) for i, j in lamps)
        
        for i, j in lamps:
            col[j] += 1
            row[i] += 1
            diag1[i-j] += 1
            diag2[i+j] += 1
            
        res = []
        for i, j in queries:
            res.append(int(row[i] > 0 or col[j] > 0 or diag1[i-j] > 0 or diag2[i+j] > 0))
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i+di, j+dj
                    if ni < 0 or ni >= N or nj < 0 or nj >= N: continue
                    if (ni, nj) in lamps:
                        row[ni] -= 1
                        col[nj] -= 1
                        diag1[ni-nj] -= 1
                        diag2[ni+nj] -= 1
                        lamps -= {(ni, nj)}
        
        return res