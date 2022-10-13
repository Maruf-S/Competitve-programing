class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        temp1,temp2 = cost[-2],cost[-1]
        for i in range(len(cost) - 3,-1,-1):
            var = temp1
            temp1 = cost[i] + min(temp1,temp2)
            temp2 = var
        return min(temp2,temp1)