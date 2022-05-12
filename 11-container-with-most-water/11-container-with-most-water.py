class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height)-1
        while(i!=j):
            max_area = max((j-i)*min(height[j],height[i]),max_area)
            if(height[i]>height[j]):
                j-=1
            else:
                i+=1
        return max_area