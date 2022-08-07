class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        k = len(arr) // 4
        return k and [x for x in arr[::k] if bisect.bisect(arr, x) - bisect.bisect_left(arr, x) > k][0] or arr[0]