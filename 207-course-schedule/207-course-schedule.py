class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for course,pre in prerequisites:
            preMap[course].append(pre)
        visited = {}
        
        def dfs(c):
            if c in visited:
                return False
            if preMap[c] == []:
                return True
            visited[c] = 1
            for i in preMap[c]:
                if dfs(i) == False:
                    return False
            preMap[c] = []
            del visited[c]
            return True
        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True