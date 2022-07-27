class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        y = sorted(Counter(arr).items(),key= lambda x : x[1])
        print(len(y))
        if len(y) < k:
            return ""
        else:
            return y[k -1][0] if y[k-1][1] == 1 else ""