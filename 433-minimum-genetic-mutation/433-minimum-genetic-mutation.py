class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def mutate(gene):
            genes = "ACGT"
            res = []
            for i in range(len(gene)):
                for G in genes:
                    if gene[i]!=G:
                        res.append(gene[:i] + G + gene[i + 1 :])
            return res
        if start == end:
            return 0
        q = deque([[start,0]])
        visit = set([start])
        bank = set(bank)
        while q:
            node,mutations = q.popleft()
            if node == end:
                return mutations
            for mut in mutate(node):
                if mut not in visit and mut in bank:
                    visit.add(mut)
                    q.append([mut,mutations + 1])
        
        return -1