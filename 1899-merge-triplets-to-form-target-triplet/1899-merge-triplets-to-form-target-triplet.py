class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for i,j,k in triplets:
            if i > target[0] or j > target[1] or k > target[2]:
                continue
            if i == target[0]:
                res.add(0)
            if j == target[1]:
                res.add(1)
            if k == target[2]:
                res.add(2)
        return len(res) == 3