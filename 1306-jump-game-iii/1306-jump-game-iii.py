class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = [start]
        visited = set()
        
        while queue:
            u = queue.pop(0)
            if arr[u] == 0:
                return True
            visited.add(u)
            
            nextjump = u + arr[u]
            if nextjump < len(arr) and nextjump not in visited:
                if arr[nextjump] == 0:
                    return True
                visited.add(nextjump)
                queue.append(nextjump)

            nextjump = u - arr[u]
            if nextjump >= 0 and nextjump not in visited:
                if arr[nextjump] == 0:
                    return True
                visited.add(nextjump)
                queue.append(nextjump)
        return False
