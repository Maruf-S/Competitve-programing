class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        supplies = set(supplies)
        indegree = defaultdict(int)
        for rec,ing in zip(recipes,ingredients):
            for i in ing:
                adj[i].append(rec)
                indegree[rec] += 1
        q = deque([i for i in supplies])
        res = []
        while q:
            node = q.popleft()
            
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    res.append(nei)
                    q.append(nei)
        return res