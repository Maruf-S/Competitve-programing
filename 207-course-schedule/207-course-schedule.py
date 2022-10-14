class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for x, y in prerequisites:
            adj[x].append(y)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not adj[course]:
                return True
            visited.add(course)
            res = True
            for i in adj[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True