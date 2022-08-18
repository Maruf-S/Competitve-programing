class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def canReach(idx):
            if idx in visited:
                return False
            if idx < 0 or idx >= len(arr):
                return False
            if arr[idx] == 0:
                return True
            visited.add(idx)
            return canReach(idx + arr[idx]) or canReach(idx - arr[idx])
        return canReach(start)