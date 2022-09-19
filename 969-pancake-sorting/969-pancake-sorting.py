class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def findMax(n):
            mi = 0
            for i in range(0,n):
                if arr[i] > arr[mi]:
                    mi = i
            return mi
        def flip(k):
            l = 0
            while l < k:
                arr[l],arr[k] = arr[k],arr[l]
                l += 1
                k -= 1
        res = []
        for i in range(len(arr) - 1,-1,-1):
            maxi = findMax(i + 1)
            
            if maxi != i:
                res.append(maxi + 1)
                flip(maxi)
                res.append(i + 1)
                flip(i)
        return res