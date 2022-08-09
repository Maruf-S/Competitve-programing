class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for course,prq in prerequisites:
            prereq[course].append(prq)
        res = []
        visiting = {}
        visited = {}
        def dfs(c):
            if c in visiting:
                return False
            if c in visited:
                return True
            visiting[c] = 1
            for i in prereq[c]:
                if dfs(i) == False:
                    return False
            del visiting[c]
            res.append(c)
            visited[c] = 1
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res