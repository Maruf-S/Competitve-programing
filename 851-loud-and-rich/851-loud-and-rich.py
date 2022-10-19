class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        poor_to_rich = defaultdict(list)
        answer = [-1] * len(quiet)
        
        for rich,poor in richer:
            poor_to_rich[poor].append(rich)
        
        def dfs(i):
            if answer[i] != -1:
                return answer[i]
            res = i
            for neihbour in poor_to_rich[i]:
                res = min(res,dfs(neihbour),key= lambda x: quiet[x])
            return res
        for person in range(len(quiet)):
            answer[person] = dfs(person)
        return answer
    