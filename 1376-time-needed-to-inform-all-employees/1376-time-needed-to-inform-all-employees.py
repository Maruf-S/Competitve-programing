class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = {i:[] for i in range(n)}
        for i,j in enumerate(manager):
            if j == -1:
                continue
            adj[j].append(i)
        
        q = deque([[headID,informTime[headID]]])
        mins = 0
        while q:
            for i in range(len(q)):
                node,ift = q.popleft()
                mins = max(mins,ift)
                for sub in adj[node]:
                    q.append((sub,ift + informTime[sub]))
        return mins