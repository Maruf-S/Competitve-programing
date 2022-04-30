class Solution(object):
    def maxCoins(self,piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        total_max = 0
        for i in range(len(piles)//3,len(piles),2):
            total_max+=piles[i]
        return total_max