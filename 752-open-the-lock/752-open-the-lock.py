class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        count = 0
        q = deque(["0000"])
        def getVariations(node):
            res = []
            for i in range(4):
                digit = str((int(node[i]) + 1)%10)
                res.append(node[:i] + digit + node[i+1:])
                digit = str((int(node[i]) -1 + 10)%10)
                res.append(node[:i] + digit + node[i+1:])
            return res
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                if node == target:
                    return count
                for child in getVariations(node):
                        q.append(child)
            count += 1
        return -1