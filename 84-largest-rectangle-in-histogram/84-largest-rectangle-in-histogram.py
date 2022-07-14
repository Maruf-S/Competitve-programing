class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q = []
        maxa = 0
        for i,j in enumerate(heights):
            start = i
            while q and q[-1][1] > j:
                idx,h = q.pop()
                maxa = max(maxa,(i-idx)*h)
                start = idx
            q.append([start,j])
        for i,h in q:
            maxa = max(maxa,(len(heights) - i)*h)
        return maxa

    
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         maxArea = 0
#         stack = [] # pair: (index, height)
        
#         for i, h in enumerate(heights):
#             start = i
#             while stack and stack[-1][1] > h:
#                 index, height = stack.pop()
#                 maxArea = max(maxArea, height * (i - index))
#                 start = index
#             stack.append((start, h))
        
#         for i, h in stack:
#             maxArea = max(maxArea, h * (len(heights) - i))
#         return maxArea