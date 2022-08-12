class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a,b) for a,b in connections}
        neighbors = defaultdict(list)
        visit = set()
        change = 0
        for i,j in connections:
            neighbors[i].append(j)
            neighbors[j].append(i)

        q = deque([0])
        while q:
            for i in range(len(q)):
                city = q.popleft()
                visit.add(city)
                for neighbor in neighbors[city]:
                    if neighbor in visit:
                        continue
                    if (neighbor,city) not in edges:
                        change += 1
                    q.append(neighbor)
        return change