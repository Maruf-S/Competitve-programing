class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(len(arr)*0.05)
        return sum(arr[n:len(arr)-n])/(len(arr)- (2*n))