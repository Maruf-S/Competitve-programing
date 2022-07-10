class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        removed = l =  0
        for i,j in sorted(counts.items(),key = lambda x: x[1],reverse = True):
            removed += j
            l+=1
            if removed >= len(arr)//2:
                return l