class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        indegree =defaultdict(int)
        for fr,to in relations:
            adj[fr].append(to)
            indegree[to] += 1
        h = ([(time[i - 1],i) for i in range(1,n +  1) if indegree[i] == 0])
        heapify(h)
        tim = 0
        while h:
            t,node = heappop(h)
            tim = max(tim,t)

            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heappush(h,(t + time[nei - 1],nei))
        return tim